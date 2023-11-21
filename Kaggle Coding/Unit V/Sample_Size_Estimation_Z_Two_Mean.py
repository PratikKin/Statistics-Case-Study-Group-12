import numpy as np 
import pandas as pd
import scipy.stats as stats

import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')


# Extract the 'blood_glucose_level' column from each DataFrame
population_glucose = df['blood_glucose_level']

var = np.var(population_glucose)

margin_of_error = 25
alpha = 0.05
beta = 0.20 


def calculate_sample_size(var, margin_of_error, alpha, beta):
    # Z-score corresponding to the desired confidence level
    z_a_tab = stats.norm.ppf(1 - alpha/2)
    z_b_tab = stats.norm.ppf(1 - beta)
    

    # Calculate sample size using the formula
    required_sample_size = ( (2 * var * (z_a_tab + z_b_tab)) / margin_of_error)**2

    return int(np.ceil(required_sample_size)//2)  # Round up to ensure a sufficient sample size

estimated_sample_size = calculate_sample_size(var, margin_of_error, alpha, beta)

print("Estimated sample size for 2 samples = ", estimated_sample_size)