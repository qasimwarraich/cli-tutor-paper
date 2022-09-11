import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


fig, (ax1, ax2) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)
fig.set_size_inches(5.90666, 5)
sns.set(style="ticks")

plt.xlabel("Programming Experience in Years")
plt.ylabel("Number of Participants")
plt.tight_layout()

data = np.array(
    [
        1,
        5,
        8,
        1,
        10,
        6,
        1,
        20,
        4,
        5,
        23,
        2,
        3,
        0.5,
        0,
        4,
        4,
        0,
        6,
        6,
        1,
        1,
        8,
        1,
        4,
        3,
        10,
        0.5,
        3,
        0,
        5,
        3,
        5,
        1,
    ]
)

max = int(data.max())
bins = np.arange(max + 2) - 0.5  # Aligns ticks to middle with -.5
# to have something atleast 1 greater than the max val we add 2 due to the subtraction.

sns.boxplot(x=data, ax=ax1, color="c", boxprops=dict(alpha=0.6))
sns.despine(ax=ax1, left=True)
ax1.set(yticks=[])
ax1.tick_params(axis="x", which="both", labelbottom=True)  # changes apply to the x-axis

sns.histplot(
    x=data, bins=bins, kde=True, ax=ax2, color="c", edgecolor="black", alpha=0.5
)

min_ylim, max_ylim = plt.ylim()
ax2.axvline(data.mean(), color="k", linestyle="dashed", linewidth=1)
ax2.text(
    data.mean() - 0.25,
    max_ylim * 0.6,
    "Mean: {:.2f}".format(data.mean()),
    color="k",
    zorder=5,
    backgroundcolor="white",
    rotation="vertical",
    fontsize=9,
)

median = int(np.median(data))
ax2.axvline(median, color="r", linestyle="dashed", linewidth=1)
ax2.text(
    median - 0.25,
    max_ylim * 0.6,
    "Median: {:.2f}".format(median),
    color="r",
    zorder=5,
    backgroundcolor="white",
    rotation="vertical",
    fontsize=9,
)


plt.xticks(range(max + 1))
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf")
