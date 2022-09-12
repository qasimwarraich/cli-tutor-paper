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
    "Extremely Uncomfortable",
    "Uncomfortable",
    "Neither Comfortable nor Uncomfortable",
    "Comfortable",
    "Extremely Comfortable",
]
comfort: Scale = comf

Q1 = "What is your comfort level with the command line?"


data = pd.DataFrame(
    {
        Q1: {
           1 : "Extremely Uncomfortable",
           2 : "Extremely Uncomfortable",
           3 : "Extremely Uncomfortable",
           4 : "Extremely Uncomfortable",
           5 : "Uncomfortable",
           6 : "Uncomfortable",
           7 : "Uncomfortable",
           8 : "Uncomfortable",
           9 : "Uncomfortable",
           10 : "Uncomfortable",
           11 : "Uncomfortable",
           12 : "Uncomfortable",
           13 : "Uncomfortable",
           14 : "Uncomfortable",
           15 : "Uncomfortable",
           16 : "Uncomfortable",
           17 : "Uncomfortable",
           18 : "Uncomfortable",
           19 : "Neither Comfortable nor Uncomfortable",
           20 : "Neither Comfortable nor Uncomfortable",
           21 : "Neither Comfortable nor Uncomfortable",
           22 : "Neither Comfortable nor Uncomfortable",
           23 : "Neither Comfortable nor Uncomfortable",
           24 : "Neither Comfortable nor Uncomfortable",
           25 : "Neither Comfortable nor Uncomfortable",
           26 : "Neither Comfortable nor Uncomfortable",
           27 : "Comfortable",
           28 : "Comfortable",
           29 : "Comfortable",
           30 : "Comfortable",
           31 : "Comfortable",
           32 : "Comfortable",
           33 : "Extremely Comfortable",
           34 : "Extremely Comfortable",
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

for bars, color in zip(ax.containers[1:], ["white"] + ["black"] * 3 + ["white"] * 2):
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
