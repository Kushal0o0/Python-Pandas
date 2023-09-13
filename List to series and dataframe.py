import pandas as pd

# list into series
"""values = [100, 200, 300, 400, 500]
series_values = pd.Series(data=values)
print(series_values)
series_values1 = pd.Series(data=values, index=["a", "b", "c", "d", "e"])
print(series_values1)"""

# nested list into series
"""values = [[100, 200, 300], [400, 500, 600]]
series_values = pd.Series(data=values)
print(series_values)"""

# list into dataframe
"""values = [100, 200, 300, 400, 500]              
dataframe_values = pd.DataFrame(data=values)
print(dataframe_values)"""

# nested list into dataframe
"""values = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]   # outer list becomes rows and inner list becomes columns
dataframe_values = pd.DataFrame(data=values)
print(dataframe_values)"""

"""names = ["kushal", "durga", "rahul", "harsha"]
values = [100, 200, 300, 400]
lol = [names, values]

dataframe = pd.DataFrame(data=lol)
print(dataframe.transpose())          # transpose function converts rows into columns and columns into rows"""











