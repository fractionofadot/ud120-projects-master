#!/usr/bin/python
import math

def sortRse(x):
    return x[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    dirty_data = []

    ### your code goes here
    for i in range(0, len(predictions)):
        err = net_worths[i] - predictions[i]
        rse = math.pow(err, 2)
        dirty_data.append([ages[i], net_worths[i], rse])

    cleaned_data = sorted(dirty_data, key=sortRse)
    keep = int(round(len(cleaned_data) * 0.9))
    del cleaned_data[keep:len(cleaned_data)]
    
    return cleaned_data

