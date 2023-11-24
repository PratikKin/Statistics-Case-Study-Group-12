### For Z-test for one sample
"""
Group Number : 12
"""
# libraries

import numpy as np 
import pandas as pd
import scipy.stats as stats
import os

# connecting the paths of code and dataset

for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
# reading CSV files
male_df = pd.read_csv('../Diabetes/male_glu.csv')
female_df = pd.read_csv('../Diabetes/female_glu.csv')

# Extract the 'blood_glucose_level' column from each DataFrame
male_glucose = male_df['blood_glucose_level']
female_glucose = female_df['blood_glucose_level']

#---------------------------------------------------------------------------------
# sample _p1, _p2

n1 = int(input("Give the sample size for male: "))
n2 = int(input("Give the sample size for female: "))
random_male_df = male_glucose.sample(n=n1, random_state=1)
random_female_df = female_glucose.sample(n=n2, random_state=1)

filtered_random_male = random_male_df[random_male_df < 120] 
filtered_random_female = random_female_df[random_female_df < 120] 

m1 = filtered_random_male_len = len(filtered_random_male)
m2 = filtered_random_female_len = len(filtered_random_female)

_p1 = m1/n1
_p2 = m2/n2


P = (m1 + m2)/(n1 + n2)


#---------------------------------------------------------------------------------------------
# functions

# calculate Z value
def Z_cal(p1, p2, P, n1, n2):
    diff_p = abs(p1 - p2)
    error = findError(n1, n2, P)
    z_cal = diff_p / error
    return z_cal
        
# find error term
def findError(n1, n2, P):
    Q = 1 - P
    pdt_PQ = P*Q
    sum_n1_n2 = (1/n1)+(1/n2)
    error = np.sqrt(pdt_PQ * sum_n1_n2)
    return error

# get Z tabulated value
def Z_tab(A_ci):
    z_tab = stats.norm.ppf(1 - A_ci/2)
    return z_tab

# get confidence interval
def calcCI(p1, p2, n1, n2, P):
    error = findError(n1, n2, P)
    diff_p = abs(p1 - p2)
    z_lower = diff_p - z_tab * error
    z_upper = diff_p + z_tab * error
    
    print("\nConfidence Interval:\n",z_lower," <= |p1-p2| <", z_upper)
#-------------------------------------------------------------------------------------------
# Implementation ->

# getting z calculated and tabulated values
z_tab = Z_tab(0.05)
z_cal = Z_cal(_p1, _p2, P, n1, n2)

# summarizing results
if z_cal <= z_tab:
    print("Accept H0")
else:
    print("Reject H0")
    
# getting confidence interval
calcCI(_p1, _p2,  n1, n2, P)