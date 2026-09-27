"""
Organiza o dataset Tomate × Pimentão no formato que o YOLO (Ultralytics) exige.

Estrutura de ORIGEM no Google Drive (como a equipe montou — não é alterada):

    FarmTech_Fase6/
    ├── Dataset_dividido/
    │   ├── Tomate/{Treino,Validacao,Teste}/Tomate NN.jpg
    │   └── Pimentao/{Treino,Validacao,Teste}/Pimentao NN.jpg
    └── Rotulacoes/Tomate NN.txt, Pimentao NN.txt   (formato YOLO, um .txt por imagem)

Estrutura de DESTINO criada por este script (cópias — os originais ficam intactos):

    FarmTech_Fase6/Dataset_dividido/
    ├── treino/{images,labels}/      ← 64 imagens (32 tomate + 32 pimentão)
    ├── validacao/{images,labels}/   ←  8 imagens (4 + 4)
    └── teste/{images,labels}/       ←  8 imagens (4 + 4)

O que o script faz, para cada imagem:
  1. copia a imagem para <split>/images/ com nome normalizado (ex.: "Tomate 16.jpg" → "tomate_16.jpg");
  2. procura o rótulo de mesmo nome em Rotulacoes/ ("Tomate 16.txt");
  3. valida cada linha do rótulo (5 campos, coordenadas entre 0 e 1);
  4. grava o rótulo em <split>/labels/ ("tomate_16.txt") com o índice de classe
     definido pelo NOME DO ARQUIVO: tomate = 0, pimentão = 1.

Por que o passo 4 reescreve o índice de classe: na exportação original, o índice
dentro dos .txt não corresponde à classe (há rótulos de tomate com 1 e de pimentão com 0).
O nome do arquivo segue o protocolo de captura e é a referência confiável da classe.
As coordenadas da caixa são mantidas exatamente como foram desenhadas.

Uso no Google Colab (depois de montar o Drive):
    python organizar_dataset_yolo.py --base /content/drive/MyDrive/FarmTech_Fase6

Opções:
    --dry-run   só mostra o que seria feito, sem copiar nada

Pode ser executado mais de uma vez: os arquivos de destino são sobrescritos com o
mesmo conteúdo. Nenhum arquivo é movido ou apagado. Termina com código de saída 1
se encontrar qualquer problema (rótulo faltando, linha inválida, imagem repetida).
"""

import argparse
import shutil
import sys
from collections import Counter
from pathlib import Path

# Pasta de cada classe no Drive → índice de classe no YOLO (mesma ordem do data.yaml)
CLASSES = {"Tomate": 0, "Pimentao": 1}

# Pasta de split no Drive (por classe) → pasta de split no formato YOLO
SPLITS = {"Treino": "treino", "Validacao": "validacao", "Teste": "teste"}

EXTENSOES_IMAGEM = {".jpg", ".jpeg", ".png"}


def nome_normalizado(stem: str) -> str:
    """'Tomate 16' → 'tomate_16' (sem espaços nem maiúsculas no destino)."""
    return "_".join(stem.lower().split())


def ler_rotulo(caminho: Path, classe_id: int) -> tuple[list[str], Counter, list[str]]:
    """Lê um rótulo YOLO e devolve (linhas com classe corrigida, índices originais, erros)."""
    linhas, originais, erros = [], Counter(), []
    for n, linha in enumerate(caminho.read_text().splitlines(), start=1):
        if not linha.strip():
            continue
        campos = linha.split()
        if len(campos) != 5:
            erros.append(f"{caminho.name} linha {n}: esperado 5 campos, encontrado {len(campos)}")
            continue
        try:
            coords = [float(c) for c in campos[1:]]
        except ValueError:
            erros.append(f"{caminho.name} linha {n}: coordenada não numérica")
            continue
        if not all(0.0 <= c <= 1.0 for c in coords):
            erros.append(f"{caminho.name} linha {n}: coordenada fora do intervalo 0–1")
            continue
        originais[campos[0]] += 1
        linhas.append(" ".join([str(classe_id), *campos[1:]]))
    if not linhas and not erros:
        erros.append(f"{caminho.name}: rótulo vazio (nenhuma caixa desenhada)")
    return linhas, originais, erros


def organizar(base: Path, dry_run: bool) -> int:
    origem = base / "Dataset_dividido"
    rotulos = base / "Rotulacoes"
    for pasta in (origem, rotulos):
        if not pasta.is_dir():
            print(f"❌ Pasta não encontrada: {pasta}")
            print("   Confira se o Drive está montado e se BASE_PATH aponta para FarmTech_Fase6.")
            return 1

    erros: list[str] = []
    contagem: Counter = Counter()          # (split, classe) → nº de imagens
    corrigidos = 0                         # rótulos cujo índice de classe foi reescrito
    vistos: dict[str, str] = {}            # nome normalizado → split (detecta repetição)
    rotulos_usados: set[str] = set()

    for classe, classe_id in CLASSES.items():
        for split_drive, split_yolo in SPLITS.items():
            pasta = origem / classe / split_drive
            if not pasta.is_dir():
                erros.append(f"Pasta não encontrada: {pasta}")
                continue
            destino_img = origem / split_yolo / "images"
            destino_lbl = origem / split_yolo / "labels"
            if not dry_run:
                destino_img.mkdir(parents=True, exist_ok=True)
                destino_lbl.mkdir(parents=True, exist_ok=True)

            for img in sorted(pasta.iterdir()):
                if img.suffix.lower() not in EXTENSOES_IMAGEM:
                    continue
                novo = nome_normalizado(img.stem)
                if novo in vistos:
                    erros.append(f"{img.name} aparece em mais de um split ({vistos[novo]} e {split_yolo})")
                    continue
                vistos[novo] = split_yolo

                rotulo = rotulos / f"{img.stem}.txt"
                if not rotulo.is_file():
                    erros.append(f"Rótulo faltando para {classe}/{split_drive}/{img.name} (esperado: {rotulo.name})")
                    continue
                rotulos_usados.add(rotulo.name)

                linhas, originais, erros_rotulo = ler_rotulo(rotulo, classe_id)
                erros.extend(erros_rotulo)
                if erros_rotulo:
                    continue
                if set(originais) != {str(classe_id)}:
                    corrigidos += 1

                if not dry_run:
                    shutil.copy2(img, destino_img / f"{novo}{img.suffix.lower()}")
                    (destino_lbl / f"{novo}.txt").write_text("\n".join(linhas) + "\n")
                contagem[(split_yolo, classe)] += 1

    orfaos = sorted(p.name for p in rotulos.glob("*.txt") if p.name not in rotulos_usados)

    # ---------------- Relatório ----------------
    print("Modo: SIMULAÇÃO (nada foi copiado)" if dry_run else "Modo: CÓPIA")
    print(f"Destino: {origem}/{{treino,validacao,teste}}/{{images,labels}}\n")
    print(f"{'split':<10} {'tomate':>7} {'pimentao':>9} {'total':>6}")
    for split_yolo in SPLITS.values():
        t, p = contagem[(split_yolo, "Tomate")], contagem[(split_yolo, "Pimentao")]
        print(f"{split_yolo:<10} {t:>7} {p:>9} {t + p:>6}")
    print(f"\nRótulos com índice de classe reescrito pelo nome do arquivo: {corrigidos}")
    if orfaos:
        print(f"⚠️  {len(orfaos)} rótulo(s) em Rotulacoes/ sem imagem correspondente: {', '.join(orfaos)}")
    if erros:
        print(f"\n❌ {len(erros)} problema(s) encontrado(s):")
        for e in erros:
            print(f"   - {e}")
        return 1
    print("\n✅ Dataset organizado sem erros.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--base", default="/content/drive/MyDrive/FarmTech_Fase6",
                        help="pasta FarmTech_Fase6 no Drive montado")
    parser.add_argument("--dry-run", action="store_true", help="só simula, não copia nada")
    args = parser.parse_args()
    sys.exit(organizar(Path(args.base), args.dry_run))


if __name__ == "__main__":
    main()
