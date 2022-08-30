import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.90666,3))


sns.set(style="ticks")

fig.suptitle(
    "Do you feel more or less intimidated by the command line after this interactive tutor?"
)

total = 10.0
yes = 10.0
no = 0.0

avg_yes = (yes / total) * 100
avg_no = (no / total) * 100
avgs = [avg_yes, avg_no]
data = np.array([avg_yes, avg_no])

b_total = 17.0
b_yes = 10.0
b_no = 7.0

b_avg_yes = (b_yes / b_total) * 100
b_avg_no = (b_no / b_total) * 100
b_avgs = [b_avg_yes, b_avg_no]
b_data = np.array([b_avg_yes, b_avg_no])

labels = [
    "Yes",
    "No",
]

max = int(data.max())
colors = sns.color_palette("Set3")[4:]

ax1.set_title("CLI-Tutor")
ax1.pie(
    data,
    colors=colors,
    autopct="%.2f%%",
    # explode=[0.2, 0],
    startangle=90,
)
ax2.set_title("Non Interactive Tutor")
ax2.pie(
    b_data,
    colors=colors,
    autopct="%.2f%%",
    # explode=[0.2, 0],
    startangle=90,
)
fig.legend(
    labels,
    # bbox_to_anchor=(1, -0.04),
    loc="center",
    labelspacing=0.1,
)

fig.set_constrained_layout(True)
# fig.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
