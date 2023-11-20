"""
Code written by Group 12    
"""
import numpy as np
import scipy.stats as stats
import pandas as pd
import os

for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
male_df = pd.read_csv('../Kaggle Coding/Unit II/male_glu.csv')

male_glucose = male_df['blood_glucose_level']

#---------------------------------------------------------------------------------
# functions

def subtract_median_and_get_sign(data, median): # Calculate the median
    signs = []
    positive_count = 0
    negative_count = 0

    for value in data:
        difference = value - median
        if difference > 0:
            signs.append('+')
            positive_count += 1
        elif difference < 0:
            signs.append('-')
            negative_count += 1
        else:
            signs.append('0')

    sign_cal = min(positive_count, negative_count)
    calculated_sample_size = abs(positive_count - negative_count)
    return sign_cal, calculated_sample_size

def get_median(data):
    sorted_data = sorted(data)
    median=0
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[(n - 1) // 2] + sorted_data[n // 2]) / 2
    
    return median


def get_sign_tab_value(alpha, sample_size):
    critical_value_upper = stats.binom.ppf(1 - alpha/2, sample_size, 0.5)
    critical_value_lower = stats.binom.ppf(alpha/2, sample_size, 0.5)
    
    return critical_value_lower, critical_value_upper

#---------------------------------------------------------------------------

alpha = 0.05 

median = get_median(male_glucose)
sign_cal, sample_size = subtract_median_and_get_sign(male_glucose, median)

sign_lower, sign_upper = get_sign_tab_value(alpha, sample_size)


if sign_cal <= sign_lower or sign_cal >= sign_upper:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Accept the null hypothesis: There is no significant difference between the groups.")