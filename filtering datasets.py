import pandas as pd
import numpy as np

nba = pd.read_csv(r"C:\Users\kusha\OneDrive\Desktop\DA\python\nba - nba.csv")  # "r" to convert a normal string into a raw string
df_nba = pd.DataFrame(nba).dropna(how="all")

df_nba = df_nba.astype({"Name": "category",
                        "Team": "category",
                        "Number": "uint8",
                        "Position": "category",
                        "Age": "uint8",
                        "Height": "category",
                        "Weight": "uint16",
                        "College": "category",
                        "Salary": "float32"})
df_nba.rename(columns={"Number": "Chest number", "Weight": "Weight(lbs)"}, inplace=True)


# accessing the columns directly + aggregation
print(df_nba["Chest number"].unique())
print(df_nba[["Chest number", "College"]])  # accessing multiple columns
print(df_nba["College"].value_counts())     # works like the group by function from SQL

# accessing the columns directly + filtering (single condition)
print((df_nba["Age"] > 35).sum())
more35 = df_nba["Age"] > 35
print(df_nba[more35][["Name", "College"]])     # passing the more35 variable inside the df_nba gives only the true value (like in numpy)
                                               # prints out the "Name" and "College" of players who are more than 35

# accessing the columns directly + filtering (multiple condition) and sorting and ISIN function
filters = (df_nba["Age"] <= 23) & (df_nba["Team"] == "Chicago Bulls")
print(df_nba[filters]["Salary"].mean())

filters = (df_nba["Age"] <= 25) & (df_nba["Position"].isin(["PF", "SF"]))    # ISIN functional arguments should be passed as a list
print(df_nba[filters][["Name", "Salary"]].sort_values(by="Salary", ascending=False))   # sorting by=column you want to sort by

# filter using LOC function
print(df_nba.loc[[4, 5]])   # loc[rows, columns]






