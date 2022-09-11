import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fig = plt.figure()

fig.set_size_inches(5.90666, 5)

sns.set(style="ticks")

plt.xlabel(
    "Are you interested in integrating the command line more into your day to day computer use?"
)

total = 34.0
yes = 27.0
no = 7.0

avg_yes = (yes / total) * 100
avg_no = (no / total) * 100
avgs = [avg_yes, avg_no]

data = np.array([avg_yes, avg_no])
labels = [
    "Yes",
    "No",
]

max = int(data.max())
colors = sns.color_palette("Set3")[2:7]

plt.pie(
    data,
    colors=colors,
    autopct="%.2f%%",
    explode=[0.2, 0],
    startangle=180,
)
legend_labels = ["%s, %1.2f %%" % (l, s) for l, s in zip(labels, avgs)]
plt.legend(
    legend_labels,
    bbox_to_anchor=(1, -0.04),
    loc="lower right",
    labelspacing=0.1,
)

# fig.set_constrained_layout(True)
plt.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
