"""
Code written by Group 12    
"""

# libraries
import numpy as np
import os
import pandas as pd
from scipy.stats import wilcoxon

# connecting the paths of code and dataset
for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)


# Read the CSV file
df = pd.read_csv('../Diabetes/diabetes_prediction_dataset.csv')

# Extract the 'blood_glucose_level' and 'blood_glucose_level_after' column from each DataFrame
glucose_before = df['blood_glucose_level']
glucose_after = df['blood_glucose_level_after']

# Calculate the differences
differences = glucose_after - glucose_before

# Perform the Wilcoxon signed-rank test
statistic, p_value = wilcoxon(differences)

# Print the results
print("Wilcoxon Signed-Rank Statistic:", statistic)
print("P-value:", p_value)

print("Hypothesis : \nH0 : There is a difference in the blood glucose level before and after blood glucose level. \nH1 : There is no difference in the blood glucose levels before and after blood glucose level.")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the paired samples.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the paired samples.")