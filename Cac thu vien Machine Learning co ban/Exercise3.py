import numpy as np
import pandas as pd

data_set = pd.read_csv("C:/Code/Cac thu vien Machine Learning co ban/dataset.csv")
active = dict()
print('First 50 line:')
print(data_set.head(50))
print("")
print("Date:")
print(data_set["Date"])
print("Calories (kcal):")
print(data_set["Calories (kcal)"])
print("Distance (m):")
print(data_set["Distance (m)"])

for index, value in data_set["Active Minutes"].items():
    if value > 100:
        active[index] = value 

print(active)

