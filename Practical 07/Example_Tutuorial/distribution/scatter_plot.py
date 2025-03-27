import matplotlib.pyplot as plt
import numpy as np

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]

y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)

plt.savefig("scatter_plot.png")


x2 = np.random.normal(5.0, 1.0, 1000)
y2 = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x2, y2)

plt.savefig("scatter_plot_normal.png")