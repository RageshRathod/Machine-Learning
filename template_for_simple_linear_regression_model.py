# -*- coding: utf-8 -*-
"""Template for Simple Linear Regression model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BTbIF-iSVQhpxfrr3VbyWRNBzW8FndRB

# Simple Linear Regression Model
## For Dataset which having numerical columns only

# Importing the Library
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""# Importing the Dataset and Split it into Dependant and Independant Variable"""

# Upload the dataset into google colab
dataset = pd.read_csv('Please Write Your File Name') # Please write your file name   eg:- abc.csv
x = dataset.iloc[ : , :-1].values      # Independant Variable
y = dataset.iloc[ : , -1 ].values      # Dependant Variable (The value we need to predict need to be in the last column)

"""# Splitting the Data in Testing and Training Set"""

from sklearn.model_selection  import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size =0.2,  random_state=2)
# splitting the data in train and test
# test data will be 20 % of the uploaded data

"""# Tranining the Linear Model"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()  # lr is variable assign to Linear Regression Model
lr.fit(x_train,y_train)  # lr = Linear Regression

"""# Predicting the test value"""

#  Here we are predicting the value of test data on the basis of train data
y_pred = lr.predict(x_test)

"""# Visualisation of Training and Testing Data"""

plt.scatter(x_train,y_train, color = 'red')
plt.plot(x_train, lr.predict(x_train), color = 'blue')
plt.title('Real vs Predicted data')
plt.xlabel('x value') # Put the x value ..what you have in dataset
plt.ylabel('y value') # Put the y Value .. what you have in dataset
plt.show()