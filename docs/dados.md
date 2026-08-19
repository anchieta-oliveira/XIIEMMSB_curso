# Dados

Os dados do curso ficam nas pastas `D03/data/<pdb>/` (um sistema BACE-1 por pasta) e na
tabela de pontuação `D03/scores_BSI*.csv`. Os arquivos de cálculo (`*.mop`, `*.pdb`)
podem ser baixados diretamente do repositório:

| Sistema | Ligante | Entrada MOPAC |
|---|---|---|
| [3bra](https://www.rcsb.org/structure/3BRA) (2.3 Å, 2008) | AEF  | [3bra_AEF_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/3bra/3bra_AEF_qm.mop)  |
| [4ha5](https://www.rcsb.org/structure/4HA5) (1.83 Å, 2012) | 13W | [4ha5_13W_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4ha5/4ha5_13W_qm.mop) |
| [4h3g](https://www.rcsb.org/structure/4H3G) (1.85 Å, 2012) | 10Q | [4h3g_10Q_qm.mop](https://raw.githubusercontent.com/anchieta-oliveira/XIIEMMSB_curso/main/D03/data/4h3g/4h3g_10Q_qm.mop) | 

## Tabela de pontuação (ΔG<sub>lig</sub> × IEDA)

Resultados de referência do curso (`scores_BSI.csv`): ΔG<sub>lig</sub> experimental calculado a
partir de kd/ki e o IEDA (densidade eletrônica intermolecular no complexo proteína–ligante).
As duas últimas linhas trazem o R² e o R da correlação ΔG<sub>lig</sub> × IEDA.

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
