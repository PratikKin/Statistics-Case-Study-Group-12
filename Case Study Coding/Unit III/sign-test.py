"""
Code written by Group 12    
"""
# libraries

import numpy as np
import pandas as pd
from scipy.stats import binom
import os

# connecting the paths of code and dataset
for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
# Read the CSV file
male_df = pd.read_csv('../Diabetes/male_glu.csv')
female_df = pd.read_csv('../Diabetes/female_glu.csv')

#  Extract the 'blood_glucose_level' column from DataFrame
male_glucose = male_df['blood_glucose_level']
female_glucose = female_df['blood_glucose_level']

filtered_random_male = random_male_df[random_male_df < 120] 
filtered_random_female = random_female_df[random_female_df < 120] 

# Calculate differences between paired observations
differences = [g1 - g2 for g1, g2 in zip(filtered_random_male, filtered_random_female)]

# Count positive and negative differences
positive_diff = sum(1 for diff in differences if diff > 0)
negative_diff = sum(1 for diff in differences if diff < 0)

# Perform a binomial test on the counts
n = positive_diff + negative_diff
p_value = binom.cdf(min(positive_diff, negative_diff), n, 0.5) + binom.sf(min(positive_diff, negative_diff) - 1, n, 0.5)

print(f"Positive differences: {positive_diff}")
print(f"Negative differences: {negative_diff}")
print(f"P-value: {p_value}")

# Significance level (alpha)
alpha = 0.05

# Hypothesis

print("Hypothesis: \nH0 : Median value of blood glucose level is less than 120. \nH1 : Median value of blood glucose level is more than 120")

# Compare p-value with alpha and make a decision
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")