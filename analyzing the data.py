import pandas as pd
import numpy as np

nba = pd.read_csv(r"C:\Users\kusha\OneDrive\Desktop\DA\python\nba2.csv")  # "r" to convert a normal string into a raw string
df_nba = pd.DataFrame(nba).dropna(how="all")

"""df_nba = df_nba.astype({"Name": "category",
                        "Team": "category",
                        "Number": "uint8",
                        "Position": "category",
                        "Age": "uint8",
                        "Height": "category",
                        "Weight": "float16",
                        "College": "category",
                        "Salary": "float32"})"""
df_nba.rename(columns={"Number": "Chest number", "Weight": "Weight(lbs)"}, inplace=True)

def feet_inches_to_cms(h):
    feet, inches = list(map(int, h.split("-")))
    return round((feet * 12 + inches) * 2.54, 1)

df_nba["height_in_c"] = df_nba.apply(lambda x: feet_inches_to_cms(x["Height"]), axis=1)
df_nba["Weight(KGS)"] = df_nba["Weight(lbs)"] * 0.453592
df_nba["BMI"] = df_nba["Weight(KGS)"] / (df_nba["height_in_c"]/100)**2

# grouping function
group = df_nba.groupby(by=["Team", "Position"])
group_df = group[["Salary", "Age"]].agg(["mean", "sum"]).reset_index()    # using agg function for multiple aggregation


filters = group_df["Team"] == "Los Angeles Lakers"
print(group_df[filters])                                 # filtering the records after group (remember to reset index in group)

group = df_nba.groupby(by=["Team", "Position"], as_index=False)
df_grouped = group.agg({"Age":"mean", "Salary":"sum"}).sort_values(by="Salary", ascending=False)
print(df_grouped)




