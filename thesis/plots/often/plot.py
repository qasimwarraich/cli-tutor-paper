import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()

fig.set_size_inches(5.90666, 5)

sns.set(style="ticks")

colors = sns.color_palette("colorblind")


total = 34
data = {
    "Never": 3,
    "At least once a year": 2,
    "A few times a year": 8,
    "At least once a month": 9,
    "Almost every day": 12,
}

frequency = list(data.keys())
values = list(data.values())

bars = plt.barh(frequency, values, color=colors)
for bar in bars:
    plt.text(
        bar.get_x() + 0.3, bar.get_y() + (bar.get_height()/2.0)-0.05,
        "{0:.2%}".format(bar.get_width()/ total),
        color = "white",
        weight = "bold",
    )

plt.xlabel("Number of responses")

plt.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
