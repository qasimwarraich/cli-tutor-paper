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
    "Books/ Online Documentation": 9,
    "Interactive Tutorials": 8,
    "Video Tutorials": 10,
    "University Lectures": 1,
    "Forums/ Online Groups (e.g. Discord Servers)": 1,
    "Other": 5,
}

frequency = list(data.keys())
values = list(data.values())

bars = plt.barh(frequency, values, color=colors)
for bar in bars:
    if bar.get_width() < 2:
        plt.text(
            bar.get_x() + 1.1, bar.get_y() + (bar.get_height()/2.0)-0.05,
            "{0:.2%}".format(bar.get_width()/ total),
            color = "black",
            weight = "bold",
        )
    else: 
        plt.text(
            bar.get_x() + 0.2, bar.get_y() + (bar.get_height()/2.0)-0.05,
            "{0:.2%}".format(bar.get_width()/ total),
            color = "white",
            weight = "bold",
        )


plt.xlabel("Number of responses")

fig.suptitle("What is your preferred method of learning related to\n technical topics?", wrap=True)
# plt.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
