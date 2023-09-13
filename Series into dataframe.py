import pandas as pd

names = ["kushal", "durga", "rahul", "harsha"]
values = [100, 200, 300, 400]
index = ["a", "b", "c", "d"]

"""names_series = pd.Series(names)
values_series = pd.Series(values)
data_frame = pd.DataFrame([names_series, values_series])
print(data_frame.transpose())"""


data_frame1 = pd.DataFrame({"names": names, "values": values, "id": index})  # line 6-9 can be achieved in 2 lines
data_frame1 = data_frame1.set_index("id")  # set_index function converts a proper column into a raw index
print(data_frame1)




