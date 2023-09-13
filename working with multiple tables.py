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


# joining 2 tables
avg_salary = df_nba.groupby(by=["Team"], as_index=False).agg({"Salary": "mean"})
players = df_nba[["Name", "Team", "Salary"]]


merged = pd.merge(avg_salary, players, on="Team")
print(merged)












