# -*- coding: utf-8 -*-
"""Modelling and simulation for one-day cricket.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HRnwLQh6BYAhrYUCyW-FnYjZz0vpSY76
"""

def custom_accuracy(y_test,y_pred,thresold):
    right = 0
    l = len(y_pred)
    for i in range(0,l):
        if(abs(y_pred[i]-y_test[i]) <= thresold):
            right += 1
    return ((right/l)*100)

# Importing the dataset

import pandas as pd
dataset = pd.read_csv('odi.csv.txt')
X = dataset.iloc[:,[7,8,9,12,13]].values
y = dataset.iloc[:, 14].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the dataset

from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=100,max_features=None)
reg.fit(X_train,y_train)

# Testing the dataset on trained model

y_pred = reg.predict(X_test)
score = reg.score(X_test,y_test)*100
print("R square value:" , score)
print("Custom accuracy:" , custom_accuracy(y_test,y_pred,20))

# Testing with a custom input

import numpy as np
new_prediction = reg.predict(sc.transform(np.array([[100,0,13,50,50]])))
print("Prediction score:" , new_prediction)

"""# **Dataset:**

1188 ODI matches -> odi.csv

**Each dataset consists of the following columns:**

- mid -> Each match is given a unique number
- date -> When the match happened
- venue -> Stadium where match is being played
- bat_team -> Batting team name
- bowl_team -> Bowling team name
- batsman -> Batsman name who faced that ball
- bowler -> Bowler who bowled that ball
- runs -> Total runs scored by team at that instance
- wickets -> Total wickets fallen at that instance
- overs -> Total overs bowled at that instance
- runs_last_5 -> Total runs scored in last 5 overs
- wickets_last_5 -> Total wickets that fell in last 5 overs
- striker -> max(runs scored by striker, runs scored by non-striker)
- non-striker -> min(runs scored by striker, runs scored by non-striker)
- total -> Total runs scored by batting team after first innings


**Prediction Algorithm and Accuracy:**

Algorithm Used:

*Random Forest Regression*

**Features and Label Used:**

Features: [runs,wickets,overs,striker,non-striker]

Label: [total] *italicized text*

**Accuracy in terms of [R Square Value,Custom Accuracy]:**

*ODI matches -> [79,77]*

*Note: Custom Accuracy is defined on the basis of difference between the predicted score and actual score. If this difference falls below a particular thresold, we count it as a correct prediction.*


"""

