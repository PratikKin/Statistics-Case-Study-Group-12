"""
Code written by Group 12    
"""
import numpy as np
import os
import pandas as pd
from scipy.stats import wilcoxon  # Added missing import

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Specify the correct relative path to the CSV file


# Read the CSV file
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

glucose_before = df['blood_glucose_level']
glucose_after = df['blood_glucose_level_after']

# Calculate the differences
differences = glucose_after - glucose_before

# Perform the Wilcoxon signed-rank test
statistic, p_value = wilcoxon(differences)

# Print the results
print("Wilcoxon Signed-Rank Statistic:", statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the paired samples.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the paired samples.")