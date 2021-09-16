from numpy.lib.function_base import append
import pandas as pd
from pandas.io.sql import table_exists
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.__coefficient = None
        self.__intercept = None
    
    def __append__one(self, x):
        one = np.ones((x.shape[0], 1))
        x = np.concatenate((x, one), axis=1)
        return x
    
    def __to__matrix(self, data):
        matrx = data.to_numpy()
        matrx = matrx.reshape(data.shape[0], 1)
        return matrx

    def get_slope(self):
        try:
            if self.__coefficient == None:
                raise Exception
            return self.__coefficient
        except:
            print('Model not trained yet')

    def get_intercept(self):
        try:
            if self.__intercept == None:
                raise Exception
            return self.__intercept
        except:
            print('Model not trained yet')

    def fit(self, x_train, y_train):
        x_train = self.__to__matrix(x_train)
        x_train = self.__append__one(x_train)
        y_train = self.__to__matrix(y_train)
        prod = np.dot(x_train.T, x_train)
        inner_prod = np.dot(x_train.T, y_train)
        inverse = np.linalg.pinv(prod)
        coeffs = np.dot(inverse, inner_prod)
        self.__intercept = coeffs[1][0]
        self.__coefficient = coeffs[0][0]
    
    def predict(self, x_test):
        try:
            if self.__coefficient == None or self.__intercept == None:
                raise Exception
            col_coefficients = np.array([[self.__coefficient, self.__intercept]]).T
            predict = np.dot(x_test, col_coefficients)
            return predict
        except:
            print('Model not trained yet')
    
    def compute_cost(self, x_test, y_test):
        x_test = self.__to__matrix(x_test)
        x_test = self.__append__one(x_test)
        y_test = self.__to__matrix(y_test)
        model = self.predict(x_test)
        cost = ((np.linalg.norm(y_test - model))**2)/2
        return cost

    def visualize(self, train_set, test_set):
        x_axis = np.linspace(-3, 7)
        y_axis = self.__coefficient*x_axis + self.__intercept 
        plt.plot(x_axis, y_axis, label=f"y = {self.__coefficient:.1f}x + {self.__intercept:.0f}", color="black")
        plt.scatter(train_set['x'], train_set['y'], c='r', label="Train Set")
        plt.scatter(test_set['x'], test_set['y'], c='b', label="Test Set")
        plt.xlabel("X axes")
        plt.title("Linear Regression")
        plt.ylabel("Y axes")
        plt.legend()
        plt.show()


data_set = pd.read_csv("Linear_Regression/linear_regression.csv")
train_set = data_set.head(160)
test_set = data_set.tail(40)

regressor = LinearRegression()
x_train = train_set["x"]
y_train = train_set["y"]
x_test = test_set["x"]
y_test = test_set["y"]
regressor.fit(x_train, y_train)
error_term = regressor.compute_cost(x_test, y_test)
print(f"Error term: {error_term:.3f}")
regressor.visualize(train_set, test_set)