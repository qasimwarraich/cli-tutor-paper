import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


fig, (ax1, ax2) = plt.subplots(
    2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)}
)
fig.set_size_inches(5.90666, 4)
sns.set(style="ticks")
plt.xlabel("Programming Experience in Years")
plt.ylabel("Number of Participants")
plt.tight_layout()


years = np.array([1, 5, 8, 1, 1, 6, 1, 20, 4, 5, 23, 2, 3, 0.5, 0, 4, 4])
bins = (
    np.arange(25) - 0.5
)  # Aligns ticks to middle 25 to have something more than 1 greater than the max val (23)

sns.boxplot(x=years, ax=ax1, color="c", boxprops=dict(alpha=0.6))
sns.despine(ax=ax1, left=True)
ax1.set(yticks=[])
ax1.tick_params(axis="x", which="both", labelbottom=True)  # changes apply to the x-axis

sns.histplot(
    x=years, bins=bins, kde=True, ax=ax2, color="c", edgecolor="black", alpha=0.5
)

min_ylim, max_ylim = plt.ylim()
ax2.axvline(years.mean(), color="k", linestyle="dashed", linewidth=1)
ax2.text(
    years.mean() - 0.25,
    max_ylim * 0.6,
    "Median: {:.2f}".format(years.mean()),
    color="k",
    zorder=5,
    backgroundcolor="white",
    rotation="vertical",
    fontsize=8,
)

median = int(np.median(years))
ax2.axvline(median, color="r", linestyle="dashed", linewidth=1)
ax2.text(
    median - 0.25,
    max_ylim * 0.6,
    "Median: {:.2f}".format(median),
    color="r",
    zorder=5,
    backgroundcolor="white",
    rotation="vertical",
    fontsize=8,
)


plt.xticks(range(24))
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf")
