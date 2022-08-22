# -*- coding: utf-8 -*-
"""Titanic-Machine Learning form disaster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15lidax3CW6X4ya4c8xWXl6REKQ2GDdzI

Importing the dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from google.colab import files

"""Loading Datasets"""

test = pd.read_csv("https://raw.githubusercontent.com/Abdur-Raffay/Titanic-Machine-Learning-from-Disaster/main/test.csv")
train = pd.read_csv("https://raw.githubusercontent.com/Abdur-Raffay/Titanic-Machine-Learning-from-Disaster/main/train.csv")

"""Checking Datatypes of Datasets"""

train.info()
train.head()

test.info()
test.head()

"""Checking for missing values or any bad data"""

train.isnull().sum()

test.isnull().sum()

train[train == 0].count()

test[test == 0].count()

train.Age = train.Age.fillna(train.Age.mean())
train.Fare = train.Fare.fillna(train.Fare.mean())
train.info()

test.Age = test.Age.fillna(test.Age.mean())
test.Fare = test.Fare.fillna(test.Fare.mean())
test.info()

train.drop(['Cabin'],axis = 1)

test.drop(['Cabin'],axis = 1)

"""Changing Datatypes of Columns"""

train['Sex'] = pd.factorize(train.Sex)[0]
test['Sex'] = pd.factorize(test.Sex)[0]

train['Name'] = train['Name'].astype('category').cat.codes
test['Name'] = test['Name'].astype('category').cat.codes

train['Ticket'] = train['Ticket'].astype('category').cat.codes
test['Ticket'] = test['Ticket'].astype('category').cat.codes

train['Cabin'] = train['Cabin'].astype('category').cat.codes
test['Cabin'] = test['Cabin'].astype('category').cat.codes

train['Embarked'] = train['Embarked'].astype('category').cat.codes
test['Embarked'] = test['Embarked'].astype('category').cat.codes

"""Data Visulaization"""

for i in train:
     if train[i].dtype == 'int64' or train[i].dtype == 'float64':
         plt.boxplot(train[i])
         fig = plt.figure(figsize = (3,3))
         plt.show()

for i in test:
     if test[i].dtype == 'int64' or test[i].dtype == 'float64':
         plt.boxplot(test[i])
         fig = plt.figure(figsize = (3,3))
         plt.show()

"""Logistic Regression"""

train_X = np.array(train.drop(['PassengerId','Survived'],axis = 1))
train_Y = np.array(train['Survived'])
test_X = np.array(test.drop(['PassengerId'],axis = 1))
train_X.reshape(1,-1)
train_Y.reshape(1,-1)
test_X.reshape(1,-1)
model = LogisticRegression()
model.fit(train_X,train_Y)

"""Checking Accuracy of Model"""

train_prediction = (model.predict(train_X))
score = accuracy_score(train_prediction,train_Y)
print('Score:',score)

"""Submission"""

prediction = model.predict(test_X)
output = pd.DataFrame({'PassengerId':test.PassengerId,'Survived':prediction})
output.to_csv('Submission.csv')
files.download('Submission.csv')