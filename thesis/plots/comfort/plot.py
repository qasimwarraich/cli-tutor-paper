import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plot_likert
import seaborn as sns
import typing

# fig = plt.figure(1)
# fig.set_size_inches(5.90666, 5)

plt.figure(0, figsize=(5, 5.90666))

Scale = typing.List[str]

comf: Scale = [
    "Extremely Uncomfortable",
    "Uncomfortable",
    "Neither Comfortable or Uncomfortable",
    "Comfortable",
    "Extremely Comfortable",
]
comfort: Scale = comf

Q1 = "What is your comfort level with the command line?"
Q2 = "What is your reading level?"


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
            10: "Neither Comfortable or Uncomfortable",
            11: "Neither Comfortable or Uncomfortable",
            12: "Neither Comfortable or Uncomfortable",
            13: "Comfortable",
            14: "Comfortable",
            15: "Comfortable",
            16: "Extremely Comfortable",
        },
        Q2: {
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
            10: "Neither Comfortable or Uncomfortable",
            11: "Neither Comfortable or Uncomfortable",
            12: "Neither Comfortable or Uncomfortable",
            13: "Comfortable",
            14: "Comfortable",
            15: "Comfortable",
            16: "Extremely Comfortable",
        },
    }
)

colors = sns.color_palette("coolwarm")
ax = plot_likert.plot_likert(data, comfort, plot_percentage=True, colors=colors, figsize=(5.90666, 5))

for bars, color in zip(ax.containers[1:], ["white"] + ["black"] * 2 + ["white"] * 2):
    ax.bar_label(bars, label_type="center", fmt="%.1f %%", color=color, fontsize=9)

plt.legend(loc="upper center", ncol=3, handlelength=0.5, fontsize=9, labelspacing=0.1, columnspacing=0)

# plt.show()

plt.savefig("plot.png", dpi=100)
# plt.savefig("plot.pgf", format="pgf")
plt.savefig("plot.pgf", format="pgf", bbox_inches="tight")
