import matplotlib as mpl

mpl.use("pgf")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fig = plt.figure()

fig.set_size_inches(5.90666, 5)

sns.set(style="ticks")

colors = sns.color_palette("colorblind")


total = 34
questions = [
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
    "Q9",
    "Q10",
    "Q11",
    "Q12",
    "Q13",
]

data1 = [
    100.00,
    63.16,
    94.28,
    100.00,
    63.16,
    52.64,
    52.63,
    94.28,
    94.28,
    94.28,
    78.95,
    89.47,
    89.47,
]


data2 = [
    100.00,
    46.67,
    73.34,
    93.34,
    60.00,
    20.00,
    60.00,
    66.67,
    80.00,
    100.00,
    86.67,
    93.34,
    80.47,
]

x = np.arange(len(questions))  # the label locations
width = 0.45  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh(x - width/2, data1 , width, label='Interactive')
rects2 = ax.barh(x + width/2, data2, width, label='Non-Interactive')
plt.gca().invert_yaxis()

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Questions')
ax.set_label('Percentage')
ax.set_title('Percentage of correct answers in the evaluation section')
ax.set_yticks(x, questions)
ax.legend(bbox_to_anchor=(0.6,0.5))

ax.bar_label(rects1, padding=1, label_type='center', fmt='%.2f')
ax.bar_label(rects2, padding=3, label_type='center', fmt='%.2f')

plt.tight_layout()
fig.savefig("plot.png", dpi=100)
fig.savefig("plot.pgf", format="pgf", bbox_inches="tight", transparent=True)
