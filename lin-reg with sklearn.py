# importing the packages

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics


# data preprocessing

df = pd.read_csv("data.csv")

X = df.iloc[ : , :1 ].values
Y = df.iloc[ : , 1].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=1)


# fitting model to training set

model = LinearRegression()
model.fit(x_train, y_train)


# predicting the result

y_pred = model.predict(x_test)


# error value

print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# # Visualization

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_test , model.predict(x_test), color ='blue')
plt.show()

