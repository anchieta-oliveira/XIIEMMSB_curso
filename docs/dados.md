# Dados

Os dados do curso ficam nas pastas `D03/data/<pdb>/` (um sistema BACE-1 por pasta) e na
tabela de pontuação `D03/scores_BSI*.csv`. Os arquivos de cálculo (`*.mop`, `*.pdb`)
podem ser baixados diretamente do repositório:

| Sistema | Ligante | Entrada MOPAC | Saída MOPAC |
|---|---|---|---|
| 3bra (2.3 Å, 2008) | AEF | [3bra_AEF_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/3bra/3bra_AEF_qm.mop) | [3bra_AEF_qm.pdb](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/3bra/3bra_AEF_qm.pdb) |
| 4ha5 (1.83 Å, 2012) | 13W | [4ha5_13W_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4ha5/4ha5_13W_qm.mop) | [4ha5_13W_qm.pdb](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4ha5/4ha5_13W_qm.pdb) |
| 4h3g (1.85 Å, 2012) | 10Q | [4h3g_10Q_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4h3g/4h3g_10Q_qm.mop) | [4h3g_10Q_qm.pdb](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4h3g/4h3g_10Q_qm.pdb) |

## Tabela de pontuação (ΔG × IEDA)

Resultados de referência do curso (`scores_BSI.csv`): ΔG experimental calculado a
partir de kd/ki e o IEDA (compartilhamento de densidade eletrônica proteína–ligante).
As duas últimas linhas trazem o R² e o R da correlação ΔG × IEDA.

```{csv-table}
:file: ../D03/scores_BSI.csv
:header-rows: 1
```

O arquivo `scores_BSI_results.csv` é o modelo em branco (IEDA = 0), para começar o
preenchimento do zero.

## Pequenas moléculas (dia 2)

O dataset do dia 2 fica em `D02/data/`:

- `xyz/` — geometrias de pares de moléculas com distâncias variadas (ex.:
  `22_AcOH_Uracil_1.xyz`, `1.05`, `1.10`, `1.25`, `1.5`, `2` Å);
- `orca_inp/` — entradas ORCA correspondentes (`B3LYP 6-31G*`, Mulliken nas saídas);
- `pbds/` — estrutura de referência em PDB.
