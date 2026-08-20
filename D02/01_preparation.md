# Preparação dos arquivos de entrada do MOPAC (dímero AcOH–Uracil)

Gerando o dataset de pequenas moléculas do dia 2: o dímero **ácido acético (ACY) + uracila (URA)** em seis distâncias intermoleculares, com um arquivo `.mop` de entrada para o MOPAC por distância, como os exemplos prontos da pasta `data/`.

## 1. O sistema e o dataset

É o complexo 22 do dataset S66 (par ácido acético–uracila, estabilizado por ponte de hidrogênio C=O···H–N). As duas moléculas somam 20 átomos: ácido acético (8 átomos, resíduo `ACY`) e uracila (12 átomos, resíduo `URA`).

Para estudar a **curva de dissociação**, o par é preparado em 6 separações:

| Distância (Å) | Pasta de resultados |
|---|---|
| 1.00 | `AcOH_Uracil_result/AcOH_Uracil_1/` |
| 1.05 | `AcOH_Uracil_result/AcOH_Uracil_1_05/` |
| 1.10 | `AcOH_Uracil_result/AcOH_Uracil_1_10/` |
| 1.25 | `AcOH_Uracil_result/AcOH_Uracil_1_25/` |
| 1.50 | `AcOH_Uracil_result/AcOH_Uracil_1_5/` |
| 2.00 | `AcOH_Uracil_result/AcOH_Uracil_2/` |


> **Atenção às convenções de nome:** nas pastas de resultado a distância usa sublinhado (`AcOH_Uracil_1_05`), nos arquivos `xyz` pode aparecer ponto (`22_AcOH_Uracil_1.05.xyz`). Mantenha o padrão do que você está editando.

## 2. Montando o arquivo `.mop`

### 2.1 A linha de cabeçalho

A primeira linha define o protocolo do cálculo. Mantenha as palavras-chave exatamente como estão:

```
PM6-D3H4 ALLVEC VECTOR LARGE MOZYME AUX eps=78.4 PDB 1SCF
```

| Palavra-chave | Significado |
|---|---|
| `PM6-D3H4` | Método semi-empírico PM6 com a correção de dispersão D3H4 |
| `ALLVEC` | Usar todos os orbitais de valência (exigido para elementos mais pesados) |
| `VECTOR` | Gravar os vetores (orbitais) no arquivo de saída |
| `LARGE` | Saída ampliada (mais detalhes por iteração) |
| `MOZYME` | *Linear scaling* – divide o sistema em regiões locais, acelerando o cálculo |
| `AUX` | Gerar o arquivo auxiliar `.aux` (contém as cargas usadas nas análises) |
| `eps=78.4` | Solvente implícito: água (constante dielétrica 78,4) |
| `PDB` | Lê e devolve os átomos em formato PDB |
| `1SCF` | Cálculo de ponto único (sem otimização de geometria) |

### 2.2 Os cartões de átomo

Cada átomo é uma linha com a anatomia de um registro `ATOM` de PDB. As duas moléculas ficam em **cadeias distintas** — ácido acético = cadeia `A`, resíduo 1; uracila = cadeia `B`, resíduo 2:

```
ATOM      1  C1  ACY A   1      -1.114   1.327   0.275  1.00  0.00           C
ATOM      2  O1  ACY A   1      -0.467   2.349   0.462  1.00  0.00           O
...
ATOM     13  N1  URA B   2       3.337   0.202   2.404  1.00  0.00           N
...
END
```

Campos de cada cartão, na ordem:

1. `ATOM` + número serial (1, 2, 3, ...);
2. nome do átomo (`C1`, `O1`, `N1`, `H1`, ...);
3. nome do resíduo (`ACY` ou `URA`) e o número do resíduo;
4. **cadeia** (`A` ou `B`) — é ela que separa as duas moléculas para a análise de interação do próximo tutorial;
5. coordenadas `x y z` (Å), preservadas da geometria;
6. ocupância `1.0`;
7. **carga na coluna do fator B** — comece com `0.0` se ainda não houver cargas de um cálculo prévio;
8. `PROT` e a coluna do elemento (`C`, `O`, `N`, `H`) no fim da linha.

O arquivo termina com a linha `END`. No total são **20 cartões** `ATOM` (8 do ácido acético + 12 da uracila).

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
| `*.arc` | Geometria final em formato ARC |

## 4. Checklist

Antes de executar:

- [ ] Cada molécula está em uma cadeia (`ACY A 1`, `URA B 2`) e o arquivo termina com `END`.
- [ ] 20 `ATOM` (8 do ácido acético + 12 da uracila).
- [ ] Sem águas, íons ou moléculas extras na entrada.

Depois de executar:

- [ ] `FINAL HEAT OF FORMATION` presente no `.out` (ex.: -180.36 kcal/mol em 1.00 Å, -23.72 em 2.00 Å).
- [ ] `.aux` gerado corretamente.
- [ ] O calor de formação **fica menos negativo** com o aumento da distância (menos interação).