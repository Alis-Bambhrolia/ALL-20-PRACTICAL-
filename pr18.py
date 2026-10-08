import pandas as pd
import numpy as np

data = {
    "Age": [25, 30, np.nan, 30, 45, 120],
    "Salary": [50000, 60000, 55000, 60000, 80000, 52000]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna(df["Age"].median())

df = df.drop_duplicates()

q1 = df["Age"].quantile(0.25)
q3 = df["Age"].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
df = df[df["Age"] <= upper_bound]

print("Cleaned DataFrame:\n", df)