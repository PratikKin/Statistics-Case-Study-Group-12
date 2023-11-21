### t-test for single mean small sample
"""
Group Number : 12
"""

import numpy as np 
import pandas as pd
import scipy.stats as stats

import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

new_df = df['blood_glucose_level']

#--------------------------------------------------------------------------------------------------
#functions

# get t-tabulated value
def T_tab(alpha, df, two_tailed=True):
    if two_tailed:
        alpha /= 2  # For a two-tailed test, divide alpha by 2

    t_tab = stats.t.ppf(1 - alpha, df)

    return t_tab

# calculate t-value
def t_cal(random_sample, sample_size, U0, U1): 
    diff_mean = abs(U1 - U0)
        
    error = findError(random_sample, sample_size)
    t_cal = diff_mean/error
    
    return t_cal

# get the error term
def findError(random_sample, sample_size):
    std_var = np.std(random_sample)
    error = std_var/(np.sqrt(sample_size))
    return error
    
# calculate the confidence interval
def calc_CI(random_sample, sample_size,U1, t_tab):
    error = findError(random_sample, sample_size)
    t_lower = U1 - t_tab*(error)
    t_upper = U1 + t_tab*(error)
    print("Confidence Interval : ", t_lower," <= U0 < ", t_upper)
    
#------------------------------------------------------------------------------------------------------------------------
# Implementation


U0 = df['blood_glucose_level'].mean()      #to get the mean

# Two tailed testing

print("\nHypothesis=>\n H0 : U1 = ", U0, "\nH1 : U1 != ", U0)

# get the samples
n = int(input("Give sample size : "))
random_sample = column_data.sample(n=n, random_state=1)
U1 = random_sample.mean()

t_tab = T_tab(0.05, n-1, True)

# we can work only if n < 30 =>
if(n < 30):
    t_cal = t_cal(random_sample, n, U0, U1)
    if(t_cal >= t_tab):
        print("Accept H0")
    else:
        print("Reject H0")
    calc_CI(random_sample, n, U1, t_tab)
else:
    print("Unable to calculate")
