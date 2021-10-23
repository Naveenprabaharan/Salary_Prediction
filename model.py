import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


# MODEL TRAINING:
# dataset = pd.read_csv('__demo\Salary_Data.csv')
# X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, -1].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
#  X_test = input("enter year:")
# y_pred = regressor.predict([[X_test]])
# print(y_pred)

# MODEL DEPLOYEMENT:

def salaryPrediction(hrs):
    model = pickle.load(open('__demo/reg_model.p','rb'))
    year = hrs

    y_out = model.predict([[year]])
    return y_out

