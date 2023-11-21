"""
Code written by Group 12    
"""
import numpy as np
from scipy.stats import mannwhitneyu
import os
import pandas as pd

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
male_df = pd.read_csv('../Dataset Used/male_glu.csv')
male_glucose = male_df['blood_glucose_level']



# Read the CSV files
female_df = pd.read_csv('../Diabetes/male_glu.csv')
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
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")