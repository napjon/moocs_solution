from __future__ import division

import numpy
import pandas
import statsmodels.api as sm
import sys

def complex_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associating
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a  more sophisticated heuristic
    that will use the passengers' gender and their social economical class and age 
    to predict if they survived the Titanic diaster. 
    
    You prediction should be 79% accurate or higher.
    
    If the passenger is female or if his/her socio-economical status is high AND
    if the passenger is under 18, you should assume the passenger surived.
    Otherwise, you should assume the passenger perished in the disaster.
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".
    
    You can access the socio-economical status of a passenger via passenger['Pclass']:
    High socio-economical status -- passenger['Pclass'] is 1
    Medium socio-economical status -- passenger['Pclass'] is 2
    Low socio-economical status -- passenger['Pclass'] is 3

    You can access the age of a passenger via passenger['Age'].
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survied or 0 otherwise. 

    For example, if a passenger survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    Or if a passenger perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        # 
        # your code here
        #
    return predictions

def check_accuracy(file_name):
    total_count = 0
    correct_count = 0
    df = pandas.read_csv(file_name)
    predictions = complex_heuristic(file_name)
    for row_index, row in df.iterrows():
        total_count += 1
        if predictions[row['PassengerId']] == row['Survived']:
            correct_count += 1
    return correct_count/total_count


if __name__ == "__main__":
    complex_heuristic_success_rate = check_accuracy('titanic_data.csv')
    print complex_heuristic_success_rate
    