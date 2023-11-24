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

filtered_df = new_df[new_df < 120]       #specified data

filtered_df_len = n1 = len(filtered_df)

new_df_len = len(new_df)

# finding proportions
p0 = (filtered_df_len/new_df_len)


margin_of_error = 0.03
alpha = 0.05

## -------------------------------------------------------

def calculate_sample_size(p0, margin_of_error, alpha):
    # Z-score corresponding to the desired confidence level 
    z_tab = stats.norm.ppf(1 - alpha/2)
    q0 = 1-p0
    # Calculate sample size using the formula
    required_sample_size = ((z_tab ** 2) * p0 * q0) / (margin_of_error ** 2)

    return int(np.ceil(required_sample_size))  # Round up to ensure a sufficient sample size

# --------------------------------------------------------------

# calculations
sample_size = calculate_sample_size(p0, margin_of_error, alpha)
print(f"Estimated sample size: {sample_size}")
