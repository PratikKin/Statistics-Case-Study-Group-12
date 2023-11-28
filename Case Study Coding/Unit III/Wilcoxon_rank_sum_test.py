"""
Code written by Group 12    
"""

# libraries
import numpy as np
from scipy.stats import mannwhitneyu
import os
import pandas as pd

# connecting the paths of code and dataset
for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)

# Read the CSV file
male_df = pd.read_csv('../Diabetes/male_glu.csv')
female_df = pd.read_csv('../Diabetes/male_glu.csv')

#  Extract the 'blood_glucose_level' column from DataFrame
male_glucose = male_df['blood_glucose_level']
female_glucose = female_df['blood_glucose_level']

n1 = int(input("Sampling size for male : "))
n2 = int(input("Sampling size for female : "))

random_sample1 = male_glucose.sample(n=n1, random_state=1)
random_sample2 = female_glucose.sample(n=n2, random_state=1)
# Perform the Mann-Whitney U test
statistic, p_value = mannwhitneyu(random_sample1, random_sample2)

# Print the results
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")