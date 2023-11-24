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

# Perform the Mann-Whitney U test
statistic, p_value = mannwhitneyu(male_glucose, female_glucose)

# Print the results
print("Mann-Whitney U Statistic:", statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")