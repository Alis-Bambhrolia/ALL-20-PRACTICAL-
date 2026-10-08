import pandas as pd

df = pd.read_csv("employee.csv")

print("--- Univariate Analysis (Age) ---")
print(df["Age"].dropna().describe())

print("\n--- Bivariate Analysis (Age & MonthlyIncome) ---")
print(df[["Age", "MonthlyIncome"]].dropna().describe())

print("\n--- Multivariate Analysis (Age, MonthlyIncome, TotalWorkingYears) ---")
print(df[["Age", "MonthlyIncome", "TotalWorkingYears"]].dropna().describe())