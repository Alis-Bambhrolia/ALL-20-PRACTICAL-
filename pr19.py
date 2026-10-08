import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Dharmik", "Ayan"], "Score": [90, 85]})
df2 = pd.DataFrame({"ID": [3, 4], "Name": ["Harsh", "Manan"], "Score": [88, 82]})

combined = pd.concat([df1, df2], ignore_index=True)

sliced = combined.loc[0:2, ["Name", "Score"]]
filtered = combined[combined["Score"] >= 85]
sorted_df = filtered.sort_values(by="Score", ascending=False)

combined["Normalized_Score"] = (combined["Score"] - combined["Score"].min()) / (combined["Score"].max() - combined["Score"].min())

print("Processed DataFrame:\n", combined)