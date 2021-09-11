import numpy as np
import pandas as pd

def filter_dict(dictionary, func_condition):
    result_dict = dict()
    for index, value in dictionary.items():
        if func_condition(value):
            result_dict[index] = value
    return result_dict


data_set = pd.read_csv("ML_Library/dataset.csv")
active = dict()
print('First 50 line:')
print(data_set.head(50))
print("")
read_column = lambda data_set, *cols: print(data_set[[*cols]])
read_column(data_set, "Date", "Calories (kcal)", "Distance (m)")
active = filter_dict(data_set["Active Minutes"], lambda x: x > 100)
print("Active Dictionary:", active)

