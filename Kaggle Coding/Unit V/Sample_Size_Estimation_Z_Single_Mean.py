import numpy as np 
import pandas as pd
import scipy.stats as stats

import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

new_df = df['blood_glucose_level']


population_std = np.std(new_df)   # Replace with the known population standard deviation
margin_of_error = 5  # Replace with the desired margin of error
confidence_level = 0.05  # Replace with the desired confidence level (e.g., 0.95 for 95%)


### ------------------------------------------------------------------

def calculate_sample_size(population_std, margin_of_error, alpha):
    # Z-score corresponding to the desired confidence level
    z_tab = stats.norm.ppf(1 - alpha/2)

    # Calculate sample size using the formula
    required_sample_size = ((z_tab * population_std) / margin_of_error)**2

    return int(np.ceil(required_sample_size))  # Round up to ensure a sufficient sample size

# Example usage:

sample_size = calculate_sample_size(population_std, margin_of_error, confidence_level)
print(f"Estimated sample size: {sample_size}")
