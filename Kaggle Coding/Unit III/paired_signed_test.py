"""
Code written by Group 12    
"""

import numpy as np
import os
import pandas as pd
from scipy.stats import binom_test  # Added missing import

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Specify the correct relative path to the CSV file


# Read the CSV file
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

glucose_before = df['blood_glucose_level']
glucose_after = df['blood_glucose_level_after']

n = len(glucose_after)  # we can take either glucose_after or glucose_before as the length of both is same

# Calculate the differences
differences = glucose_after - glucose_before

# Count positive and negative differences
positive_diff_count = np.sum(differences > 0)
negative_diff_count = np.sum(differences < 0)
zero_diff_count = np.sum(differences == 0)

# Perform a binomial test
total_count = len(differences)
p_value = (2*min(positive_diff_count, negative_diff_count))/(n-zero_diff_count)

# Print the results
print("Number of positive differences:", positive_diff_count)
print("Number of negative differences:", negative_diff_count)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the paired samples.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the paired samples.")