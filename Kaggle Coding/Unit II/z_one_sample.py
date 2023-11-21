### For Z-test for one sample
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



#-------------------------------------------------------------------------------------------

#Provide the Ztab value for the Z-tests
def Z_tab(A_ci, iftwoSided):         #A_ci is alpha and iftwoSided can provide with the value that if the case is one sided or two sided
    if iftwoSided == 1:
        z_tab = stats.norm.ppf(1 - A_ci/2)

    else:
        z_tab = stats.norm.ppf(1 - A_ci)
    
    return z_tab
    
# Calculate Z value.
def Z_cal(random_sample, sample_size, U0, U1): 
    diff_mean = abs(U1 - U0)
    
    error = findError(random_sample, sample_size)
    z_cal = diff_mean/error
    
    return z_cal

#To find the error term
def findError(random_sample, sample_size):
    std_var = np.std(random_sample)
    error = std_var/(np.sqrt(sample_size))
    return error
    
# To calculate confidence interval
def calc_CI(random_sample, sample_size,U1, z_tab):
    error = findError(random_sample, sample_size)
    z_lower = U1 - z_tab*(error)
    z_upper = U1 + z_tab*(error)
    print("Confidence Interval : ", z_lower," <= U0 < ", z_upper)
    
#--------------------------------------------------------------------------------------------

U0 = df['blood_glucose_level'].mean()      #to get the mean



print("\nHypothesis =>\n H0 : U0 = ", U0, "\n","H1 : U0 !=", U0, "\n")

sample_size = int(input("Give sample size : "))
random_sample = new_df.sample(n=sample_size, random_state=1)
U1 = random_sample.mean()

z_tab = Z_tab(0.05, 0)
z_cal = Z_cal(random_sample, sample_size, U0 ,U1)

if z_cal <= z_tab:
    print("Accept H0")
else:
    print("Reject H0")
    