import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 52]
categories = ["A", "B", "C", "D", "E"]
values = [15, 30, 45, 10, 25]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y, color="blue", marker="o")
axs[0, 0].set_title("Line Plot")

axs[0, 1].bar(categories, values, color="green")
axs[0, 1].set_title("Bar Chart")

axs[1, 0].hist(y, bins=5, color="purple", edgecolor="black")
axs[1, 0].set_title("Histogram")

axs[1, 1].scatter(x, y, color="red")
axs[1, 1].set_title("Scatter Plot")

plt.tight_layout()
plt.show()