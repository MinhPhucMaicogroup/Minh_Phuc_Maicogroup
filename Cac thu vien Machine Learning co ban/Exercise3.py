import numpy as np
import pandas as pd

data_set = pd.read_csv("C:/Code/Cac thu vien Machine Learning co ban/dataset.csv")
active = dict()
print('First 50 line:')
print(data_set.head(50))
print(data_set[["Date", "Calories (kcal)", "Distance (m)"]])

for index, value in data_set["Active Minutes"].items():
    if value > 100:
        active[index] = value 

print("Active Dictionary: ")
print(active)

