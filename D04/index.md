# Dia 4 — Plots

## Objetivos

- Gerar uma matriz de densidade eletrônica intermolecular a partir dos resultados
  do MOPAC.
- Visualizar a densidade eletrônica por átomo em uma estrutura 3D.
- Representar a matriz como um mapa 2D (*heatmap*).
- Comparar as contribuições de diferentes orbitais moleculares.

## Conteúdo

- Matriz de IED por par de átomos.
- Mapa 3D no formato PDB para visualização no VMD.
- Mapa 2D por átomo e por resíduo.

## 1. Preparação

Os comandos deste dia devem ser executados a partir da pasta `D04`:

```bash
cd D04
conda activate IEDA
```

Antes de calcular a matriz, é necessário ter:

- o PDB de saída do MOPAC, em `D03/data/<sistema>/`;
- o arquivo auxiliar `.aux`, gerado pelo MOPAC a partir do arquivo `.mop`;
- o IEDA instalado e disponível no ambiente Conda.


O cabeçalho do arquivo `.mop` deve conter a palavra-chave `AUX`. O arquivo
gerado será `3bra_AEF_qm.aux` na mesma pasta da entrada.

> Os arquivos `.aux` são resultados locais do cálculo e não fazem parte do
> dataset versionado. Cada participante deve gerá-los em sua própria máquina.

## 2. Matriz de densidade eletrônica

O comando `matrix` calcula a contribuição IED para cada par de átomos da
estrutura. A matriz é simétrica: a posição `(i, j)` representa a contribuição
entre os átomos `i` e `j`, e a posição `(j, i)` contém o mesmo valor.

Calcule a matriz do complexo `3bra/AEF` usando o arquivo `.aux` do MOPAC:

```bash
IEDA matrix \
  --pdb ../D03/data/3bra/3bra_AEF_qm.pdb \
  --qm ../D03/data/3bra/3bra_AEF_qm.aux \
  --qm_sof mopac \
  --out IED_3bra \
  --out_format npy
```

O parâmetro `--qm_sof mopac` informa ao IEDA como interpretar o arquivo
quântico. O parâmetro `--out IED_3bra` cria um diretório para os resultados e
`--out_format npy` solicita o formato binário do NumPy, usado diretamente pelos
comandos de visualização.

Confira os arquivos gerados:

```bash
ls -lh IED_3bra/
```

O arquivo principal para os plots é:

```text
IED_3bra/IED_mulliken.npy
```

Para confirmar que a matriz pode ser lida e conferir suas dimensões:

```bash
python - <<'PY'
import numpy as np

ied = np.load("IED_3bra/IED_mulliken.npy")
print("dimensões:", ied.shape)
print("mínimo:", ied.min())
print("máximo:", ied.max())
print("simétrica:", np.allclose(ied, ied.T))
PY
```

O número de linhas e colunas deve ser igual ao número de átomos do PDB. A
simetria da matriz é uma verificação importante antes de gerar os gráficos.

## 3. Mapa 3D para o VMD

O comando `map_3D` lê a matriz e escreve um novo PDB com a contribuição IED de
cada átomo no campo beta. Esse campo pode ser usado pelo VMD para colorir a
estrutura de acordo com a densidade eletrônica intermolecular.

```bash
IEDA map_3D \
  --pdb ../D03/data/3bra/3bra_AEF_qm.pdb \
  --ied IED_3bra/IED_mulliken.npy \
  --pdbout IED_3bra/3bra_AEF_IED_map.pdb \
  --intrachain False
```

Abra o PDB gerado no VMD 2:

```bash
vmd IED_3bra/3bra_AEF_IED_map.pdb
```

No VMD, selecione a representação `NewCartoon` para a proteína e use o campo
`Beta` como critério de coloração. Para visualizar os valores de forma mais
clara, também é possível usar `Licorice` ou `VDW` na região do ligante.

O parâmetro `--intrachain False` evita que o mapa seja dominado por interações
entre átomos da mesma cadeia. Assim, o mapa enfatiza a contribuição entre a
proteína e o ligante, que estão nas cadeias `A` e `X` dos complexos do curso.

## 4. Mapa 2D (*heatmap*)

A matriz também pode ser representada como um mapa 2D. Primeiro gere o mapa
por átomo:

```bash
IEDA plot_heatmap \
  --ied IED_3bra/IED_mulliken.npy \
  --pdb ../D03/data/3bra/3bra_AEF_qm.pdb \
  --intrachain False \
  --per_residue True \
  --savefig True \
  --plot False \
  --figname IED_3bra/heatmap_IED_3bra_atom.png
```

O mapa por resíduo facilita a identificação dos resíduos da proteína que mais
contribuem para o reconhecimento do ligante. Compare os eixos do gráfico com
as seleções usadas no tutorial do Dia 3 (`chain A` e `chain X`).

## 5. Repetição para os outros complexos

Depois de validar o primeiro sistema, repita o mesmo fluxo para `4ha5/13W` e
`4h3g/10Q`, alterando os caminhos e o diretório de saída:

```bash
IEDA matrix \
  --pdb ../D03/data/4ha5/4ha5_13W_qm.pdb \
  --qm ../D03/data/4ha5/4ha5_13W_qm.aux \
  --qm_sof mopac \
  --out IED_4ha5 \
  --out_format npy

IEDA matrix \
  --pdb ../D03/data/4h3g/4h3g_10Q_qm.pdb \
  --qm ../D03/data/4h3g/4h3g_10Q_qm.aux \
  --qm_sof mopac \
  --out IED_4h3g \
  --out_format npy
```

Para cada sistema, use o respectivo `IED_mulliken.npy` nos comandos `map_3D` e
`plot_heatmap`. Não misture a matriz de um sistema com o PDB de outro: a ordem
dos átomos da matriz deve ser exatamente a mesma do PDB usado no cálculo.

## 6. Checklist

- [ ] O arquivo `.aux` foi gerado pelo MOPAC com a palavra-chave `AUX`.
- [ ] O comando `IEDA matrix` terminou sem erro.
- [ ] `IED_mulliken.npy` foi criado no diretório do sistema.
- [ ] As dimensões da matriz correspondem ao número de átomos do PDB.
- [ ] A matriz é simétrica.
- [ ] O PDB do mapa 3D foi aberto no VMD.
- [ ] O heatmap por átomo foi gerado.
- [ ] O heatmap por resíduo foi gerado.
