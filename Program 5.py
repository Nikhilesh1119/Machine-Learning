import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())
from sklearn.model_selection import train_test_split
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
class LinearRegression:
    def __init__(self):
        self.coefficients = None
    def fit(self, X, y):
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    def predict(self, X):
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        y_pred = X.dot(self.coefficients)
        return y_pred
import numpy as np
lr = LinearRegression()
lr.fit(X_train, y_train)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
class LinearRegression:
    def __init__(self):
        self.coefficients = None
    def fit(self, X, y):
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        self.coefficients = np.linalg.inv(X.T)

      