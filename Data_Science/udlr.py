
import numpy as np
import pandas
from ggplot import *

def normalize_features(array):
    """Normalized the features in the data set"""
    array_normalized = (array-array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()
    
    return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function fiven a set of features/values,
    and the values for our thetas
    """
    m = len(values)
    H = np.dot(features, theta)
    cost = (np.square(H-values)).sum().(2*m)
    
    return cost

def gradient_descent(features,values,theta, alpha, num_iterations)
    """
    Perform gradient descent given a data set with an arbitrary number of features
    """
    m = len(values)
    cost_history = []
    
    for i in range(num_iterations):
        J = compute_cost(features, values, theta)
        cost_history.append(J)
        H = np.dot(features, theta)
        GD = (alpha/m)*np.dot((values-H), features)
        theta = np.add(theta,GD)
    
    return theta, pandas.Series(cost_history)

def plot_cost_history(alpha, cost_history):
    """
    Viewing plot for our cost history
    
    For function called only in the function it self, print this return function
    
    """
    cost_df = pandas.DataFrame({
        'Cost_History': cost_history,
        'Iteration': range(len(cost_history))
})
    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
            geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )
    
    
def predictions(features,values,alpha,num_iterations):

    
    
    m = len(values)
    
    features,mu,sigma = normalize_features(features)
    
    #create one features with one. This acts like constanta, bias unit.
    features['ones'] = np.ones(m)
    
    #If we look here, features and values is turned into np object array
    #So we can do vectorize computation, without even to use (np.add, np.subtract, etc)
    features_array = np.array(features)
    values_array = np.array(values).flatten()#return a copy of the array collapsed into one dimension
    

    
    #Init theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array,
                                                            values_array,
                                                            theta_gradient_descent,
                                                            alpha,
                                                            num_iterations
                                                            )
    
    plot = None
    #Uncomment to see
    #plot = plot_cost_history(alpha, cost_history)
    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot
    
def separate_data_from_predictions(dataframe):
        """
    dataframe itself is a pandas dataframe called weather_turnstile in the Udacity Class
    We use the predictions function to predict ridership NYC subway using linear regresion with gradient descent
    
    Separate the input from predictions to encapsulate it
    """
        
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = dataframe[['rain','precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]

    #Set MANUAL alpha, num_iter
    alpha = 0.1
    num_iterations = 75
    
    return predictions(features,values,alpha,num_iterations)