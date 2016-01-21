from prediction import predictions

import pandas as pd
import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    up =  np.square(np.subtract(data,predictions)).sum()
    down = np.square(np.subtract(data,np.dot(np.mean(data),np.ones(np.array(data).shape)))).sum()
    #r_squared = 1 - np.square(np.subtract(data,predictions)).sum()/np.square(data-np.mean(data).sum()
    r_squared = 1 - up/down

    #####NEATER ANSWER  BY GRADER. BUT I DON'T USE IT. JUST PUT IT HERE AS PART OF MY OWN DOCUMENTATION
    #_mean = np.mean(data)
    #_a = np.sum(np.square(data - predictions))
    #_b = np.sum(np.square(data - _mean))
    #r_squared = 1.0 - (_a / _b)
    return r_squared


if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predictions = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predictions)
    print r_squared