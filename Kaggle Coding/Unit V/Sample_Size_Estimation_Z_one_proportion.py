import numpy as np 
import pandas as pd
import scipy.stats as stats

import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

new_df = df['blood_glucose_level']

filtered_df = new_df[new_df < 120]       #specified data

filtered_df_len = n1 = len(filtered_df)

new_df_len = len(new_df)

p0 = (filtered_df_len/new_df_len)


margin_of_error = 0.03
confidence_level = 0.05

## -------------------------------------------------------

def calculate_sample_size(p0, margin_of_error, alpha):
    # Z-score corresponding to the desired confidence level
    z_tab = stats.norm.ppf(1 - alpha/2)
    q0 = 1-p0
    # Calculate sample size using the formula
    required_sample_size = ((z_tab ** 2) * p0 * q0) / (margin_of_error ** 2)

    return int(np.ceil(required_sample_size))  # Round up to ensure a sufficient sample size

sample_size = calculate_sample_size(p0, margin_of_error, confidence_level)
print(f"Estimated sample size: {sample_size}")
