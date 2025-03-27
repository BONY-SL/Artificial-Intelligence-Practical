import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 250)

plt.hist(x, 25)
plt.savefig("histogram.png")  # Save as an image

x2 = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x2, 100)
plt.savefig("histogram2.png")
