import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)

plt.savefig("scatter_plot_normal.png")