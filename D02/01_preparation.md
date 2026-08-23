# Preparação dos arquivos de entrada do MOPAC (dímero AcOH–Uracil)

Gerando o dataset de pequenas moléculas do dia 2: o dímero **ácido acético (ACY) + uracila (URA)** em seis distâncias intermoleculares, com um arquivo `.mop` de entrada para o MOPAC por distância, como os exemplos prontos da pasta `data/`.

## 1. O sistema e o dataset

É o complexo 22 do dataset S66 (par ácido acético–uracila, estabilizado por ponte de hidrogênio C=O···H–N). As duas moléculas somam 20 átomos: ácido acético (8 átomos, resíduo `ACY`) e uracila (12 átomos, resíduo `URA`).

Para estudar a **curva de dissociação**, o par é preparado em 6 separações:

| Distância | Pasta de resultados |
|---|---|
| 1.00 | `AcOH_Uracil_result/AcOH_Uracil_1/` |
| 1.05 | `AcOH_Uracil_result/AcOH_Uracil_1_05/` |
| 1.10 | `AcOH_Uracil_result/AcOH_Uracil_1_10/` |
| 1.25 | `AcOH_Uracil_result/AcOH_Uracil_1_25/` |
| 1.50 | `AcOH_Uracil_result/AcOH_Uracil_1_5/` |
| 2.00 | `AcOH_Uracil_result/AcOH_Uracil_2/` |


## 2. Montando o arquivo `.mop`

### 2.1 A linha de cabeçalho

A primeira linha define o protocolo do cálculo. Mantenha as palavras-chave exatamente como estão:

```
PM6-D3H4 ALLVEC VECTOR LARGE MOZYME AUX eps=78.4 PDB 1SCF
```

| Palavra-chave | Significado |
|---|---|
| [`PM6-D3H4`](https://openmopac.net/Manual/pm6_d3h4.html) | Método PM6 com correções para dispersão (D3) e ligações de hidrogênio (H4). |
| [`ALLVEC`](https://openmopac.net/Manual/allvec.html) | Imprime todos os orbitais moleculares (MOs). |
| [`VECTORS`](https://openmopac.net/Manual/vectors.html) | Imprime energias e coeficientes dos orbitais moleculares. |
| [`LARGE`](https://openmopac.net/Manual/large.html) | Aumenta a quantidade de informações na saída e em arquivos auxiliares. |
| [`MOZYME`](https://openmopac.net/Manual/mozyme.html) | Usa orbitais localizados para acelerar cálculos de sistemas grandes. |
| [`AUX`](https://openmopac.net/Manual/auxiliary.html) | Gera o arquivo `.aux` com dados eletrônicos e estruturais do cálculo. |
| [`EPS=78.4`](https://openmopac.net/Manual/eps.html) | Define solvente implícito com constante dielétrica 78,4, típica da água. |
| [`PDB`](https://openmopac.net/Manual/pdb.html) | Indica que a geometria está no formato PDB. |
| [`1SCF`](https://openmopac.net/Manual/one_scf.html) | Executa cálculo de ponto único, sem otimização da geometria. |


### 2.2 Os cartões de átomo

Cada átomo é uma linha com `ATOM`. As duas moléculas ficam em **cadeias distintas** — ácido acético = cadeia `A`, resíduo 1; uracila = cadeia `B`, resíduo 2:

```
ATOM      1  C1  ACY A   1      -1.114   1.327   0.275  1.00  0.00           C
ATOM      2  O1  ACY A   1      -0.467   2.349   0.462  1.00  0.00           O
...
ATOM     13  N1  URA B   2       3.337   0.202   2.404  1.00  0.00           N
...
END
```

O arquivo termina com a linha `END`. No total são **20 átomos** (`ATOM`) (8 do ácido acético + 12 da uracila).

```
ATOM      2  HN1 GLY A  58      38.123 -15.054  30.775  1.0   3.18      PROT H
│         │  │   │   │   │      │      │      │      │     │          │     │
│         │  │   │   │   │      x      y      z    ocup. carga     "PROT" elem.
│         │  │   │   │   └── nº. do resíduo
│         │  │   │   └────── cadeia (sobrenome)
│         │  │   └────────── nome do resíduo
│         │  └────────────── nome do átomo
│         └───────────────── número serial
└─────────────────────────── "ATOM"
```

## 3. Executando o cálculo

Para cada distância, na pasta do sistema:

```bash
mopac 22_AcOH_Uracil_1_05.mop
```

Arquivos gerados:

| Arquivo | Conteúdo útil |
|---|---|
| `*.out` | Log completo; `FINAL HEAT OF FORMATION` (kcal/mol) |
| `*.aux` | Arquivo auxiliar com as cargas (usado pelo IEDA no próximo tutorial) |
| `*.arc` | Arquivo de saída de arquivamento (geometria/estrutura resultante). |

## 4. Checklist

Antes de executar:

- [ ] 20 `ATOM` (8 do ácido acético + 12 da uracila).
- [ ] Sem águas, íons ou moléculas extras na entrada.

Depois de executar:

- [ ] `FINAL HEAT OF FORMATION` presente no `.out` (ex.: -180.36 kcal/mol em 1.00, -23.72 em 2.00).
- [ ] `.aux` gerado corretamente.