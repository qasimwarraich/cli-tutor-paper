import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fig = plt.figure()

fig.set_size_inches(5.90666, 5)

sns.set(style="ticks")

plt.xlabel("Computer Science University")

data = np.array([29.41, 29.41, 29.41, 0, 11.76, 0])
labels = [
    "No CS Degree",
    "Bachelors's Degree",
    "Master's Degree",
    "Doctorate Degree",
    "Other Engineering Degree",
    "Yes but did not finish",
]

max = int(data.max())
colors = sns.color_palette("Set3")[0:7]

plt.pie(data, colors=colors, autopct="%.1f%%")
legend_labels = ["%s, %1.1f %%" % (l, s) for l, s in zip(labels, data)]
plt.legend(
    legend_labels,
    bbox_to_anchor=(0.88, -0.04),
    loc="lower right",
    # handlelength=0.5,
    labelspacing=0.1,
)

# fig.set_constrained_layout(True)
plt.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
