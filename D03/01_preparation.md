# Preparação dos arquivos de entrada do MOPAC

Convertendo um PDB de complexo proteína–ligante em um arquivo `.mop` de entrada para o MOPAC, como os exemplos da pasta `data/` (3bra, 4ha5, 4h3g).

## 1. O que vamos gerar

Um arquivo de entrada do MOPAC é um texto com:

1. uma linha de cabeçalho com as palavras-chave do cálculo;
2. os átomos do sistema em formato de cartão (linhas que lembram um PDB);
3. a linha `END`.

Exemplo real (`data/4h3g/4h3g_10Q_qm.mop`):

```
PM6-D3H4 ALLVEC VECTOR LARGE  MOZYME eps=78.4 PDB 1SCF AUX


ATOM      1  N   GLY A  58      37.596 -15.755  30.227  1.0  -1.84      PROT N
ATOM      2  HN1 GLY A  58      38.123 -15.054  30.775  1.0   3.18      PROT H
...
ATOM   6028  C1  10Q X 900      22.035  10.640  21.238  1.0   2.81      PROT C
...
ATOM   6080  H20 10Q X 900      30.818  11.162  20.695  1.0   1.70      PROT H
END
```

## 2. A linha de cabeçalho

Palavra por palavra:

| Palavra-chave | Significado |
|---|---|
| `PM6-D3H4` | Método semi-empírico PM6 com a correção de dispersão D3H4 |
| `ALLVEC` | Usar todos os orbitais de valência (exigido p/ elementos mais pesados) |
| `VECTOR` | Gravar os vetores (orbitais) no arquivo de saída |
| `LARGE` | Saída ampliada (mais detalhes por iteração) |
| `MOZYME` | *Linear scaling* – divide o sistema em regiões locais; essencial para macromoléculas (proteína inteira) |
| `eps=78.4` | Solvente implícito: água (constante dielétrica 78,4) |
| `PDB` | Lê e devolve os átomos em formato PDB |
| `1SCF` | Cálculo de ponto único (sem otimização de geometria). Onde for otimizar, trocar por outra palavra-chave |
| `AUX` | Gerar o arquivo auxiliar `.aux` (contém as cargas usadas nas análises) |

> **Importante:** não altere a linha de cabeçalho dos arquivos fornecidos. Ela define o protocolo do curso.

## 3. O formato dos cartões de átomo

Cada átomo é uma linha de 79 caracteres com a mesma anatomia de um registro `ATOM` de PDB:

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

### O ligante

O ligante é padronizado em todas as linhas:

- nome do resíduo = código do ligante (ex.: `10Q`);
- **cadeia `X`** e **nº. de resíduo 900**, para nunca colidir com a numeração da proteína;


## 4. Passo a passo da conversão

### 4.1 Obter o complexo

Baixe o PDB do complexo (ex.: `4h3g` no RCSB) e separe mentalmente as partes: proteína + ligante + demais partes cristalográficas (água, íons).

### 4.2 Definir estados de protonação

Para o pH fisiológico do dia 1:

- Adicione os hidrogênios que faltam no PDB (no nosso protocolo, o **N-terminal** fica com três hidrogênios: `HN1/HN2/HN3`; o C-terminal fica desprotonado, como em `3bra`, que começa no resíduo `-4`).
- Escolha o estado dos resíduos ionizáveis (Asp/Glu desprotonados, Lys/Arg protonados, His conforme o ambiente).
- O ligante também deve estar no estado de protonação correto (ex.: carga de sistema +1 nos CSVs).


### 4.3 Montar o arquivo .mop

Junte: cabeçalho + linha em branco + cartões + `END`. Salve com a convenção de nomes do curso, ex.: `4h3g_10Q_qm.mop`.

## 5. Executando o cálculo

Na pasta com o `.mop`, execute:

```bash
mopac 4h3g_10Q_qm.mop
```

Arquivos gerados:

| Arquivo | Conteúdo útil |
|---|---|
| `*.out` | Log completo: energia, iterações SCF, cargas, orbitais |
| `*.aux` | Arquivo auxiliar com as cargas/índices usados nas análises posteriores |

## 6. Checklist de conferência

Antes de executar o MOPAC:

- [ ] Carga total do sistema (soma das cargas por coluna) consistente com a coluna "Carga sys." dos CSVs.
- [ ] Sem `HOH`/água (se não forem desejadas) ou íons de cristal na entrada; o PDB deve estar preparado (protonado, geometria adequada, etc.).
- [ ] (Opcional) Ligante em cadeia única, exemplo `X`.

Depois de executar (resultados):
- [ ] Saída `.out` terminou com convergência SCF (sem erros).
- [ ] Arquivo `.aux` gerado corretamente.
- [ ] Conferir as cargas do ligante e da proteína na saída `.out` (cargas totais consistentes com os CSVs).