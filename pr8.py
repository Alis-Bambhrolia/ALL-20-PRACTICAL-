import pandas as pd

df = pd.read_csv("employee.csv")
age_series = df["Age"].dropna()

print("Mean:", age_series.mean())
print("\nDescribe Summary:\n", age_series.describe())
print("Median:", age_series.median())
print("Mode:", age_series.mode()[0])
print("Variance:", age_series.var())

max_age = age_series.max()
min_age = age_series.min()
print(f"Age range of employee in company: {min_age} to {max_age}")

q1 = age_series.quantile(0.25)
q3 = age_series.quantile(0.75)
iqr = q3 - q1
print("IQR of Age:", iqr)