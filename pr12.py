import numpy as np
from scipy import stats

data = np.array([12, 15, 18, 22, 20, 25, 28, 30, 18, 24])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True).mode[0])
print("Skewness:", stats.skew(data))
print("Kurtosis:", stats.kurtosis(data))

t_stat, p_val = stats.ttest_1samp(data, 20)
print(f"\nT-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")