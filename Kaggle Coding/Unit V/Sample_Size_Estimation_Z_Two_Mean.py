# libraries
import numpy as np 
import pandas as pd
import scipy.stats as stats
import os

# connecting the paths of code and dataset
for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)

# reading CSV files        
df = pd.read_csv('../Diabetes/diabetes_prediction_dataset.csv')


# getting only one column with name = "blood_glucose_level" 
population_glucose = df['blood_glucose_level']

var = np.std(population_glucose)

margin_of_error = 5
alpha = 0.05
beta = 0.20 

# -----------------------------------------------------------------------
def calculate_sample_size(var, margin_of_error, alpha, beta):
    # Z-score corresponding to the desired confidence level
    z_a_tab = stats.norm.ppf(1 - alpha/2)
    z_b_tab = stats.norm.ppf(1 - beta)
    

    # Calculate sample size using the formula
    required_sample_size = ( (2 * var * (z_a_tab + z_b_tab)) / margin_of_error)**2

    return int(np.ceil(required_sample_size)//2)  # Round up to ensure a sufficient sample size

# ------------------------------------------------------------------------
# calculations
estimated_sample_size = calculate_sample_size(var, margin_of_error, alpha, beta)

print("Estimated sample size for 2 samples = ", estimated_sample_size)