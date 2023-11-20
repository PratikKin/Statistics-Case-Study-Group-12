### For Z-proportion test for one sample 
"""
Group Number : 12
"""

import numpy as np 
import pandas as pd
import scipy.stats as stats

import os

for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
df = pd.read_csv('../Diabetes/diabetes_prediction_dataset.csv')

new_df = df['blood_glucose_level']

#-------------------------------------------------------------------------
# to get p0

new_df_len = len(new_df)

filtered_df = new_df[new_df < 120]       #specified data

filtered_df_len = n1 = len(filtered_df)

p0 = (filtered_df_len/new_df_len)

#-------------------------------------------------------------------------
# to get p
n = int(input("Give the sample size : "))
random_df = new_df.sample(n=n, random_state=1)

random_df_len = len(random_df)

filtered_random = random_df[random_df < 120] 

filtered_random_len = len(filtered_random)

p = (filtered_random_len/random_df_len)

print("\nThe proportion of people with blood sugar level less than 120 is : ",p0)

#------------------------------------------------------------------------------
#Functions

def Z_cal(p, p0, n):
    diff_p = p - p0
    error = findError(p0, n)
    z_cal = diff_p / error
    return z_cal

def findError(p0, n):
    q0 = 1 - p0
    pdt_pq = p0*q0
    
    error = np.sqrt(pdt_pq/(n-1))
    return error

def Z_tab(A_ci):
    z_tab = stats.norm.ppf(1 - A_ci/2)
    return z_tab

def calcCI(p0, n):
    error = findError(p0, n)
    z_lower = p0 - z_tab*error
    z_upper = p0 + z_tab*error
    
    print("\nConfidence Interval : \n",z_lower, " <= p < ", z_upper)

#---------------------------------------------------------------------------------
# Implementation

z_cal = Z_cal(p, p0, n)
z_tab = Z_tab(0.05)

if(z_cal <= z_tab):
    print("\nAccept H0")
else:
    print("\nReject H0")
    
calcCI(p0, n)