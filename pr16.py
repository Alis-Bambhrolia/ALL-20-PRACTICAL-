import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x), label="Normal Distribution")
plt.plot(np.linspace(0, 5, 100), expon.pdf(np.linspace(0, 5, 100)), label="Exponential Distribution")
plt.title("Continuous Probability Distributions")
plt.legend()
plt.show()

sample_means = []
for _ in range(1000):
    sample = np.random.exponential(scale=1.0, size=30)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=30, density=True, color="lightgreen", edgecolor="black")
plt.title("Central Limit Theorem (Distribution of Sample Means)")
plt.show()