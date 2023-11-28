# libraries
import numpy as np 
import pandas as pd
import scipy.stats as stats
import os

# connecting the paths of code and dataset
for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)

# reading CSV file
df = pd.read_csv('../Diabetes/diabetes_prediction_dataset.csv')

# getting only one column with name = "blood_glucose_level" 
new_df = df['blood_glucose_level']


population_std = np.std(new_df)
margin_of_error = 0.5  # Replace with the desired margin of error
alpha = 0.05  


### ------------------------------------------------------------------

def calculate_sample_size(population_std, margin_of_error, alpha):
    # Z-score corresponding to the desired confidence level
    z_tab = stats.norm.ppf(1 - alpha/2)

    # Calculate sample size using the formula
    required_sample_size = ((z_tab * population_std) / margin_of_error)**2

    return int(np.ceil(required_sample_size))  # Round up to ensure a sufficient sample size

## -------------------------------------------------------------------
# Calculations

sample_size = calculate_sample_size(population_std, margin_of_error, alpha)
print(f"Estimated sample size: {sample_size}")
