# This is Tyler's first attempt at training & submitting a model to Kaggle.
# Based on https://www.dataquest.io/m/32/getting-started-with-kaggle

import pandas
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
import numpy as np

###################
""" Training set """
###################

""" Clean up data """
titanic = pandas.read_csv("data.nosync/train.csv")

# Age: Replace missing vals w/ median from training set
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

# Sex: Codify male = 0, female = 1
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

# Embarked: replace missing vals w/ S
titanic['Embarked'] = titanic['Embarked'].fillna('S')
# Embarked: codify S = 0, C = 1, Q = 2
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

# Fare: Replace missing w/ median from TEST set
titanic['Fare'] = titanic['Fare'].fillna(titanic['Fare'].median())

""" Train model """

# The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# Initialize our algorithm class
alg = LogisticRegression(random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
# Take the mean of the scores (because we have one for each fold)
print(scores.mean())



#############################################
"""Prepare test set data """
titanic_test = pandas.read_csv("data.nosync/test.csv")

# Age: Replace missing vals w/ median from training set
titanic_test['Age'] = titanic_test['Age'].fillna(titanic['Age'].median())

# Sex: Codify male = 0, female = 1
titanic_test.loc[titanic_test['Sex'] == 'male', 'Sex'] = 0
titanic_test.loc[titanic_test['Sex'] == 'female', 'Sex'] = 1

# Embarked: replace missing vals w/ S
titanic_test['Embarked'] = titanic_test['Embarked'].fillna('S')
# Embarked: codify S = 0, C = 1, Q = 2
titanic_test.loc[titanic_test['Embarked'] == 'S', 'Embarked'] = 0
titanic_test.loc[titanic_test['Embarked'] == 'C', 'Embarked'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'Q', 'Embarked'] = 2

# Fare: Replace missing w/ median from TEST set
titanic_test['Fare'] = titanic_test['Fare'].fillna(titanic_test['Fare'].median())


#############################################
""" Make predictions on test data set """
# Initialize the algorithm class
alg = LogisticRegression(random_state=1)

# Train the algorithm using all the training data
alg.fit(titanic[predictors], titanic["Survived"])

# Make predictions using the test set
predictions = alg.predict(titanic_test[predictors])

# Create a new dataframe with only the columns Kaggle wants from the data set
submission = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": predictions
    })
submission.to_csv('submission1.txt', index=False)
