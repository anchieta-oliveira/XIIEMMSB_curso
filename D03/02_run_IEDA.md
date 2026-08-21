# Calcular a Densidade Eletrônica Intermolecular

Cálculo da densidade eletrônica de interação (**IED – Interacting Electron Density**) entre a BACE-1 e o ligante dos três complexos do curso, com a ferramenta IEDA, e preenchimento da tabela de correlação com o ΔG experimental.

## 1. Objetivo

Para cada sistema (`3bra`/AEF, `4ha5`/13W, `4h3g`/10Q) queremos a **quantidade de densidade eletrônica compartilhada entre a proteína (cadeia A) e o ligante (cadeia X)**. Esse valor (IED) entra na coluna `IEDA` do `scores_BSI.csv`, que correlaciona ΔG experimental × compartilhamento de densidade eletrônica.

## 2. Pré-requisitos

- Ferramenta **IEDA** instalada (`IEDA --help` deve listar as opções).
- O cálculo **MOPAC já executado na etapa anterior** do tutorial: ao rodar `mopac 3bra_AEF_qm.mop`, a palavra-chave `AUX` do cabeçalho gera o arquivo `3bra_AEF_qm.aux`. Esse arquivo é o `--qm` do IEDA — ele não está na pasta de dados porque é gerado em cada máquina.
- Arquivos da pasta `data/<pdb>/`:
  - `*_qm.mop` — entrada do MOPAC (não precisa mais, o `.aux` já saiu dela);
  - `*_qm.pdb` — saída do MOPAC em formato PDB, com a **mesma ordem e numeração de átomos do `.aux`** (é o `--pdb`).


> **Importante:** o `--pdb` e o `--qm` devem descrever o *mesmo* sistema, na *mesma* ordem de átomos. Por isso usamos sempre o `*_qm.pdb` (saída) e o `*_qm.aux` (saída) gerados juntos.

## 3. Cálculo do IED proteína–ligante (`two_sel`)

Gre o arquivo auxiliar do complexo `3bra/AEF`, por exemplo, com:

```bash
mopac ../D03/data/3bra/3bra_AEF_qm.mop
```

Para cada sistema, execute na pasta `data/<pdb>/`:

```bash
# 3bra / AEF
IEDA two_sel --pdb 3bra_AEF_qm.pdb --qm 3bra_AEF_qm.aux --qm_sof mopac --sel_a "chain A" --sel_b "chain X"

# 4ha5 / 13W
IEDA two_sel --pdb 4ha5_13W_qm.pdb --qm 4ha5_13W_qm.aux --qm_sof mopac --sel_a "chain A" --sel_b "chain X"

# 4h3g / 10Q
IEDA two_sel --pdb 4h3g_10Q_qm.pdb --qm 4h3g_10Q_qm.aux --qm_sof mopac --sel_a "chain A" --sel_b "chain X"
```

Explicação dos argumentos:

| Argumento | Valor usado | Papel |
|---|---|---|
| `--pdb` | `<pdb>_<lig>_qm.pdb` | Geometria (PDB) |
| `--qm` | `<pdb>_<lig>_qm.aux` | Resultado do cálculo QM (MOPAC) com a densidade eletrônica |
| `--qm_sof` | `mopac` | Software do cálculo QM (nosso caso é MOPAC; o exemplo genérico usa `orca`) |
| `--sel_a` | `"chain A"` | Primeira seleção: a proteína |
| `--sel_b` | `"chain X"` | Segunda seleção: o ligante |

Sobre as seleções:

- Nos nossos arquivos a proteína está sempre na **cadeia A** e o ligante na **cadeia X** (resíduo 900).
- Alternativa equivalente: `--sel_b "resname 10Q"` (ou `AEF`/`13W`), selecionando pelo nome do resíduo do ligante.
- O `two_sel` calcula o IED **entre as duas seleções**, exatamente o compartilhamento proteína–ligante que queremos.

Anote o valor de IED retornado pelo `two_sel` para cada sistema (0.0821…, 0.2067…, 0.2346… no gabarito).

## 4. Preenchimento do CSV

A tabela `scores_BSI.csv` já contém o ΔG experimental (calculado a partir de kd/ki, em kcal/mol). Complete a coluna `IEDA` com o valor do `two_sel` de cada sistema:

| PDB | Ligante | ΔG (kcal/mol) | IEDA (coluna a preencher) |
|---|---|---|---|
| 3bra | AEF | -3.680 | |
| 4ha5 | 13W | -9.868 | |
| 4h3g | 10Q | -11.211 | |

Depois, recalcule as linhas finais do arquivo:

- `R2 RSQ` — R² da correlação ΔG × IEDA;
- `R` — coeficiente de correlação linear (com sinal).

> `scores_BSI_results.csv` é o modelo em branco (IEDA = 0, R² = 0): serve para começar do zero. O `scores_BSI.csv` contém os valores de referência do curso — use-o para conferir seus números.

**Gabarito (valores de referência do curso):**

| PDB | IEDA |
|---|---|
| 3bra | 0.082126066 |
| 4ha5 | 0.206749409 |
| 4h3g | 0.23466 |

R² = 0.999978321, R = -0.999989161.

## 5. Interpretação da correlação

### 5.1 Regressão ΔG × IEDA (`plot_regression.py`)

O script `plot_regression.py` (na pasta `D03/`) lê o `scores_BSI.csv`, ajusta a regressão linear entre o ΔG de ligação experimental e o IED, calcula o coeficiente de correlação de Pearson **R** e o valor de *p*, e rotula cada ponto com o PDB:

```bash
python plot_regression.py
```

O gráfico é salvo como `reg_DG_vs_IEDA.png`: quanto maior a densidade eletrônica intermolecular entre proteína e ligante, mais negativo o ΔG de ligação.

- Maior densidade eletrônica intermolecular no complexo proteína-ligante apresenta correlação com afinidade molecular (expressa pelo ΔG de ligação) .
- O ΔG de ligação mais negativo (`4h3g` > `4ha5` > `3bra`) acompanha o **maior IED**.
- O sistema com maior densidade eletrônica intermolecular (4h3g) apresenta ΔG de ligação mais negativo.

