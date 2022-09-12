import matplotlib as mpl
from plot_likert.colors import TRANSPARENT

mpl.use("pgf")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plot_likert
import seaborn as sns
import typing

Scale = typing.List[str]

comf: Scale = [
    "Extremely Ineffective",
    "Ineffective",
    "Neither Ineffective nor Effective",
    "Effective",
    "Extremely Effective",
]
comfort: Scale = comf

Q1 = "How effective would you rate reading books and documentation as a learning medium for you?"


data = pd.DataFrame(
    {
        Q1: {
           1 : "Extremely Ineffective",
           2 : "Ineffective",
           3 : "Ineffective",
           4 : "Ineffective",
           5 : "Ineffective",
           6 : "Ineffective",
           7 : "Ineffective",
           8 : "Ineffective",
           9 : "Ineffective",
           10 : "Ineffective",
           11 : "Ineffective",
           12 : "Neither Ineffective nor Effective",
           13 : "Neither Ineffective nor Effective",
           14 : "Neither Ineffective nor Effective",
           15 : "Neither Ineffective nor Effective",
           16 : "Neither Ineffective nor Effective",
           17 : "Neither Ineffective nor Effective",
           18 : "Effective",
           19 : "Effective",
           20 : "Effective",
           21 : "Effective",
           22 : "Effective",
           23 : "Effective",
           24 : "Effective",
           25 : "Effective",
           26 : "Effective",
           27 : "Effective",
           28 : "Effective",
           29 : "Effective",
           30 : "Effective",
           31 : "Effective",
           32 : "Extremely Effective",
           33 : "Extremely Effective",
           34 : "Extremely Effective",
        },
    }
)

colors = sns.color_palette("coolwarm_r")
colors[0] = TRANSPARENT

# ax = plot_likert.plot_likert(data, comfort, plot_percentage=True, colors=colors, figsize=(5.90666, 5))
ax = plot_likert.plot_likert(
    data,
    comfort,
    plot_percentage=True,
    colors=colors,
    width=0.4
)

for bars, color in zip(ax.containers[1:], ["black"] + ["black"] * 3 + ["black"] * 2):
    ax.bar_label(bars, label_type="center", fmt="%.2f%%", color=color, fontsize=8.5)

plt.legend(
    loc="upper center",
    ncol=3,
    # handlelength=0.5,
    fontsize=9,
    labelspacing=0.1,
    columnspacing=0,
    bbox_to_anchor=(0.2, 1.4),
)

ax.figure.set_size_inches(7, 2.5)
# plt.show()

plt.savefig("plot.png", dpi=100)
plt.savefig("plot.pgf", format="pgf", bbox_inches="tight")
