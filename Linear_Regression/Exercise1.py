import pandas as pd
from pandas.io.sql import table_exists
import numpy as np
import matplotlib.pyplot as plt

def concatenate(x):
    one = np.ones((x.shape[0], 1))
    x = np.concatenate((x, one), axis=1)
    return x


data_set = pd.read_csv("Linear_Regression/linear_regression.csv")
training_set = data_set.head(160)
testing_set = data_set.tail(40)

x_bar = training_set['x'].to_numpy().reshape((160, 1))
xbar = concatenate(x_bar)
y_training = training_set['y'].to_numpy().reshape((160, 1))
x_tranpose = xbar.T
A = np.dot(x_tranpose, xbar)
b = np.dot(x_tranpose, y_training)
A_inverse = np.linalg.pinv(A)
W = np.dot(A_inverse, b)

x_test = testing_set['x'].to_numpy().reshape((40, 1))
x_test = concatenate(x_test)
y_hat = np.dot(x_test, W)
y_test = testing_set['y'].to_numpy().reshape((40, 1))
error = round((np.linalg.norm(y_test - y_hat)**2)/2, 5)
x_axis = np.linspace(-3, 7)
y_axis = W[0][0]*x_axis + W[1][0]
print("Error: ", error)

plt.plot(x_axis, y_axis, label=f"y = {round(W[0][0], 1)}x + {round(W[1][0], 1)}")
plt.scatter(data_set['x'], data_set['y'], c='r')
plt.xlabel("X axis")
plt.title("Linear Regression")
plt.ylabel("Y axis")
plt.legend()
plt.show()



