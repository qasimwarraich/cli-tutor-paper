import matplotlib as mpl
from plot_likert.colors import TRANSPARENT

mpl.use("pgf")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plot_likert
import seaborn as sns
import typing

# fig = plt.figure(1)
# fig.set_size_inches(5.90666, 5)

# plt.figure(0, figsize=(5, 5.90666))

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
Q2 = "What is your reading level?"
Q3 = "What is your spamming level?"


data = pd.DataFrame(
    {
        Q1: {
            0: "Extremely Uncomfortable",
            1: "Extremely Uncomfortable",
            2: "Uncomfortable",
            3: "Uncomfortable",
            4: "Uncomfortable",
            5: "Uncomfortable",
            6: "Uncomfortable",
            7: "Uncomfortable",
            8: "Uncomfortable",
            9: "Uncomfortable",
            10: "Neither Comfortable nor Uncomfortable",
            11: "Neither Comfortable nor Uncomfortable",
            12: "Neither Comfortable nor Uncomfortable",
            13: "Neither Comfortable nor Uncomfortable",
            14: "Extremely Uncomfortable",
            15: "Comfortable",
            16: "Extremely Comfortable",
        },
        Q2: {
            0: "Extremely Uncomfortable",
            1: "Extremely Uncomfortable",
            2: "Extremely Uncomfortable",
            3: "Extremely Uncomfortable",
            4: "Extremely Uncomfortable",
            5: "Extremely Uncomfortable",
            6: "Extremely Uncomfortable",
            7: "Uncomfortable",
            8: "Uncomfortable",
            9: "Uncomfortable",
            10: "Neither Comfortable nor Uncomfortable",
            11: "Neither Comfortable nor Uncomfortable",
            12: "Neither Comfortable nor Uncomfortable",
            13: "Comfortable",
            14: "Comfortable",
            15: "Comfortable",
            16: "Extremely Comfortable",
        },
        Q3: {
            0: "Extremely Uncomfortable",
            1: "Extremely Uncomfortable",
            2: "Uncomfortable",
            3: "Uncomfortable",
            4: "Uncomfortable",
            5: "Uncomfortable",
            6: "Uncomfortable",
            7: "Uncomfortable",
            8: "Uncomfortable",
            9: "Uncomfortable",
            10: "Neither Comfortable nor Uncomfortable",
            11: "Neither Comfortable nor Uncomfortable",
            12: "Neither Comfortable nor Uncomfortable",
            13: "Comfortable",
            14: "Comfortable",
            15: "Comfortable",
            16: "Extremely Comfortable",
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
    width=0.7
)

for bars, color in zip(ax.containers[1:], ["white"] + ["black"] * 3 + ["white"] * 2):
    ax.bar_label(bars, label_type="center", fmt="%.1f%%", color=color, fontsize=8.5)

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
