import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

sns.set_theme(style="darkgrid", context="paper", palette="deep", font="sans-serif")

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "scores_S66.csv")
df_clean = df.dropna(subset=["MP2/cc-pVTZ CP(kcal/mol)", "IED"])

f, ax = plt.subplots(figsize=(6, 5))
sns.regplot(x=df_clean["MP2/cc-pVTZ CP(kcal/mol)"], y=df_clean["IED"],
            line_kws={"alpha": 0.7, "lw": 2}, scatter_kws={"s": 20}, ax=ax)

if len(df_clean) >= 2:
    res = stats.pearsonr(x=df_clean["MP2/cc-pVTZ CP(kcal/mol)"], y=df_clean["IED"])
    correlation = res[0]
    pr = format(res[1], ".1e")

    ax.text(0.05, 0.95, f"R: {correlation:.2f}\np: {pr}",
            transform=ax.transAxes,
            verticalalignment="top", horizontalalignment="left",
            color="#3f8abe", style="italic")

ax.set_xlabel("ΔE MP2/cc-pVTZ CP (kcal/mol)")
ax.set_ylabel("IED (a.u.)")

f.tight_layout()
f.savefig(HERE / "reg_IED_vs_MP2.png", dpi=600)