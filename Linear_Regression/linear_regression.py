import pandas as pd
from pandas.io.sql import table_exists
import numpy as np
import matplotlib.pyplot as plt

def coefficient(x, y):
    dot_square = np.dot(x.T, x)
    dot_prod = np.dot(x.T, y)
    inverse = np.linalg.pinv(dot_square)
    coeffs = np.dot(inverse, dot_prod)
    return coeffs


def append_one(x):
    one = np.ones((x.shape[0], 1))
    x = np.concatenate((x, one), axis=1)
    return x


data_set = pd.read_csv("Linear_Regression/linear_regression.csv")
train_set = data_set.head(160)
test_set = data_set.tail(40)
compute_cost = lambda output, model: ((np.linalg.norm(output - model))**2)/2

x_train = np.array(train_set['x'].values)
x_train = x_train.reshape((160, 1))
x_train = append_one(x_train)
y_train = np.array(train_set['y'].values)
y_train = y_train.reshape((160, 1))
coeffs = coefficient(x_train, y_train)

x_output = np.array(test_set['x'].values)
x_output = x_output.reshape((40, 1))
x_output = append_one(x_output)
model = np.dot(x_output, coeffs)
y_output = np.array(test_set['y'].values)
y_output = y_output.reshape((40, 1))
cost = compute_cost(y_output, model)
print(f"Error term: {cost:.3f}")

x_axis = np.linspace(-3, 7)
intercept = coeffs[1][0]
slope = coeffs[0][0]
y_axis = slope*x_axis + intercept 
plt.plot(x_axis, y_axis, label=f"y = {slope:.1f}x + {intercept:.0f}")
plt.scatter(data_set['x'], data_set['y'], c='r')
plt.xlabel("X axes")
plt.title("Linear Regression")
plt.ylabel("Y axes")
plt.legend()
plt.show()



