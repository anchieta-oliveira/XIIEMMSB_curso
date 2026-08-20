# Calcular a Densidade Eletrônica Intermolecular

Cálculo do **IED (Interacting Electronic Density)** entre o ácido acético (cadeia A) e a uracila (cadeia B), preenchimento do `scores_S66.csv` e análise da **curva de dissociação** do dímero.

## 1. Objetivo

Para cada distância (1.00, 1.05, 1.10, 1.25, 1.50, 2.00) queremos a **densidade eletrônica intermolecualr entre as duas moléculas**, calculada pelo IEDA. O valor entra na coluna `IED` do `scores_S66.csv`, que guarda também o ΔE da dissociação pela energia de referência `MP2/cc-pVTZ CP`. Com isso montamos:

- a **curva de dissociação**: ΔE × distância;
- o **compartilhamento × distância**: IED × distância;
- a **correlação ΔE × IED**: quanto mais densidade eletrônica é compartilhada, mais forte é a interação (e mais negativo o ΔE).

### O que é o IED?

O IED é a medida de **quanto da densidade eletrônica de um sistema é compartilhada entre dois fragmentos**. Ele é obtido a partir do resultado do cálculo quântico (o arquivo `.aux`) e da geometria (o PDB, que define onde estão os átomos de cada fragmento). A ferramenta **IEDA** faz esse particionamento e devolve o valor do IED para a seleção escolhida, no nosso caso, entre as duas moléculas.

## 2. Pré-requisitos

- Ferramenta **IEDA** instalada (`IEDA --help` deve listar as opções).
- Os cálculos **MOPAC executados na etapa anterior**: os arquivos `*.aux` gerados por `mopac 22_AcOH_Uracil_<d>.mop` (palavra-chave `AUX` no cabeçalho). Os resultados de referência estão em `data/AcOH_Uracil_result/AcOH_Uracil_<d>/`.
- Para cada distância, o par PDB + `.aux` **da mesma distância** (mesma ordem de átomos).

## 3. Cálculo do IED AcOH–uracila (`two_sel`)

As duas moléculas estão em cadeias distintas (A = ácido acético, B = uracila), então o IED intermolecular é dado pelo `two_sel` entre `resid 1` e `resid 2` ou `chain A` e `chain B`:

```bash
# d = 1.00 
IEDA two_sel --pdb pbds/22_AcOH_Uracil_1.pdb --qm AcOH_Uracil_result/AcOH_Uracil_1/22_AcOH_Uracil_1.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 2"

# d = 1.05 
IEDA two_sel --pdb pbds/22_AcOH_Uracil_1_05.pdb --qm AcOH_Uracil_result/AcOH_Uracil_1_05/22_AcOH_Uracil_1_05.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 2"

# d = 1.10
IEDA two_sel --pdb pbds/22_AcOH_Uracil_1_10.pdb --qm AcOH_Uracil_result/AcOH_Uracil_1_10/22_AcOH_Uracil_1_10.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 2"

# d = 1.25 
IEDA two_sel --pdb pbds/22_AcOH_Uracil_1_25.pdb --qm AcOH_Uracil_result/AcOH_Uracil_1_25/22_AcOH_Uracil_1_25.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 2"

# d = 1.50 
IEDA two_sel --pdb pbds/22_AcOH_Uracil_1_5.pdb --qm AcOH_Uracil_result/AcOH_Uracil_1_5/22_AcOH_Uracil_1_5.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 2"

# d = 2.00 
IEDA two_sel --pdb pbds/22_AcOH_Uracil_2.pdb --qm AcOH_Uracil_result/AcOH_Uracil_2/22_AcOH_Uracil_2.aux --qm_sof mopac --sel_a "resid 1" --sel_b "resid 1"
```

Anote o IED de cada distância.

Explicação dos argumentos:

| Argumento | Valor usado | Papel |
|---|---|---|
| `--pdb` | `pbds/22_AcOH_Uracil_<d>.pdb` | Geometria (PDB por distância) |
| `--qm` | `AcOH_Uracil_result/AcOH_Uracil_<d>/22_AcOH_Uracil_<d>.aux` | Resultado do cálculo QM (MOPAC) com a densidade eletrônica |
| `--qm_sof` | `mopac` | Software do cálculo QM |
| `--sel_a` | `"resid 1"` | Primeira seleção: ácido acético |
| `--sel_b` | `"resid 2"` | Segunda seleção: uracila |

> **Importante:** o `--pdb` e o `--qm` devem descrever o *mesmo* sistema, na *mesma* ordem de átomos — por isso os pares são sempre da mesma distância.

## 4. Preenchimento do CSV

A tabela `scores_S66.csv` já traz o ΔE de referência (MP2/cc-pVTZ em kcal/mol). Complete a coluna `IED` — ela fica vazia de propósito no modelo entregue:

| nome | MP2/cc-pVTZ CP (kcal/mol) | IED (coluna a preencher) |
|---|---|---|
| 22_AcOH-Uracil (1.00) | -19.49 | |
| 22_AcOH-Uracil (1.05) | -19.15 | |
| 22_AcOH-Uracil (1.10) | -18.41 | |
| 22_AcOH-Uracil (1.25) | -15.14 | |
| 22_AcOH-Uracil (1.50) | -9.86 | |
| 22_AcOH-Uracil (2.00) | -4.15 | |

## 5. Curva de dissociação

### 5.1 ΔE × distância

Com a coluna MP2 e as distâncias, plote ΔE (kcal/mol) contra a distância. Espere um mínimo em ~1.0–1.1 (máxima interação, ponte de hidrogênio C=O···H–N) e ΔE subindo em direção a zero conforme o par se separa.

### 5.2 IED × distância (correlação)

Plote o IED (sua coluna) contra a energia calculada com MP2/cc-pVTZ CP (kcal/mol). A densidade eletrônica intermoelcualr deve acompanhar a interação.


```{note}
Gráficos
```

## 6. Checklist

- [ ] Os 6 PDBs e os 6 `.aux` usados são das mesmas distâncias (nomes casam).
- [ ] Seleções corretas: resid `1` (AcOH) × resid `2` (uracila).
- [ ] Coluna `IED` do `scores_S66.csv` preenchida com os valores do `two_sel`.
- [ ] IED decrescente com a distância (no mínimo, sem valores anômalos entre distâncias vizinhas).
- [ ] Correlação ΔE × IED negativa (IED alto ⇔ ΔE mais negativo).