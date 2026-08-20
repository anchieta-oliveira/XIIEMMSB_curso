import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

sns.set_theme(style="darkgrid", context="paper", palette="deep", font="sans-serif")

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "scores_BSI.csv")
df_clean = df[pd.to_numeric(df["DG (kcal/mol)"], errors="coerce").notna()]
df_clean = df_clean.dropna(subset=["DG (kcal/mol)", "IEDA"])

f, ax = plt.subplots(figsize=(6, 5))
sns.regplot(x=df_clean["DG (kcal/mol)"], y=df_clean["IEDA"],
            line_kws={"alpha": 0.7, "lw": 2}, scatter_kws={"s": 40}, ax=ax)

for _, row in df_clean.iterrows():
    ax.annotate(row["PDB"], (row["DG (kcal/mol)"], row["IEDA"]),
                textcoords="offset points", xytext=(6, 4), fontsize=9)

if len(df_clean) >= 2:
    res = stats.pearsonr(x=df_clean["DG (kcal/mol)"], y=df_clean["IEDA"])
    correlation = res[0]
    pr = format(res[1], ".1e")

    ax.text(0.95, 0.95, f"R: {correlation:.2f}\np: {pr}",
            transform=ax.transAxes,
            verticalalignment="top", horizontalalignment="right",
            color="#3f8abe", style="italic")

ax.set_xlabel("ΔG exp. (kcal/mol)")
ax.set_ylabel("IEDA (a.u.)")

f.tight_layout()
f.savefig(HERE / "reg_DG_vs_IEDA.png", dpi=600)