import pandas as pd
from pandas.io.sql import table_exists
import numpy as np
import matplotlib.pyplot as plt

data_set = pd.read_csv("Linear_Regression/linear_regression.csv")
training_set = data_set.head(160)
testing_set = data_set.tail(40)

x_training = training_set['x'].to_numpy().reshape((160, 1))
one = np.ones((x_training.shape[0], 1))
xbar = np.concatenate((x_training, one), axis=1)
y_training = training_set['y'].to_numpy().reshape((160, 1))
x_tranpose = xbar.T
A = np.dot(x_tranpose, xbar)
b = np.dot(x_tranpose, y_training)
A_inv = np.linalg.pinv(A)
W = np.dot(A_inv, b)

x_test = testing_set['x'].to_numpy().reshape((40, 1))
one = np.ones((x_test.shape[0], 1))
x_test = np.concatenate((x_test, one), axis=1)
y_hat = np.dot(x_test, W)
y_test = testing_set['y'].to_numpy().reshape((40, 1))
error = (np.linalg.norm(y_test - y_hat)**2)/2
error = round(error, 2)
x_axis = np.linspace(-2.5, 6.5)
y_axis = W[0][0]*x_axis + W[1][0]
print("Error: ", error)

plt.plot(x_axis, y_axis, label="Fitting Line")
plt.scatter(data_set['x'], data_set['y'], c='r')
plt.xlabel("X axis")
plt.title("Linear Regression")
plt.ylabel("Y axis")
plt.legend()
plt.show()



