import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("Pandas Series:\n", s)

data = {
    "Name": ["Dharmik", "Ayan", "Harsh", "Manan"],
    "Department": ["IT", "CS", "IT", "CS"],
    "Salary": [60000, 55000, 58000, 52000]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)

filtered_df = df[df["Salary"] > 54000]
print("\nFiltered (Salary > 54000):\n", filtered_df)

grouped = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", grouped)