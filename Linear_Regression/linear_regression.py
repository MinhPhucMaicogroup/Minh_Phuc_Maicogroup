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


def to_matrix(series):
    matrx = series.to_numpy()
    matrx = matrx.reshape(matrx.shape[0], 1)
    return matrx


data_set = pd.read_csv("Linear_Regression/linear_regression.csv")
train_set = data_set.head(160)
test_set = data_set.tail(40)
compute_cost = lambda output, model: ((np.linalg.norm(output - model))**2)/2

x_train = to_matrix(train_set["x"])
x_train = append_one(x_train)
y_train = to_matrix(train_set["y"])
coeffs = coefficient(x_train, y_train)

x_output = to_matrix(test_set["x"])
x_output = append_one(x_output)
model = np.dot(x_output, coeffs)
y_output = to_matrix(test_set["y"])
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



