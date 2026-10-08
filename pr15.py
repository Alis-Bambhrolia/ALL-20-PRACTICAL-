import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

n, p = 10, 0.5
x_bin = np.arange(0, 11)
prob_bin = binom.pmf(x_bin, n, p)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(x_bin, prob_bin, color="skyblue")
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Successes")
plt.ylabel("Probability")

mu = 4
x_poi = np.arange(0, 15)
prob_poi = poisson.pmf(x_poi, mu)

plt.subplot(1, 2, 2)
plt.bar(x_poi, prob_poi, color="salmon")
plt.title("Poisson Distribution (lambda=4)")
plt.xlabel("Events")
plt.ylabel("Probability")

plt.tight_layout()
plt.show()