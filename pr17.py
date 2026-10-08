import numpy as np
from scipy import stats

scores = np.array([85, 88, 90, 78, 92, 85, 87, 91, 82, 89])
null_mean = 80
alpha = 0.05

t_stat, p_val = stats.ttest_1samp(scores, null_mean)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val < alpha:
    print("Reject the null hypothesis: Significant difference detected.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")