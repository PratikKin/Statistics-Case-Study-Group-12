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
male_df = pd.read_csv('../Diabetes/male_glu.csv')
female_df = pd.read_csv('../Diabetes/female_glu.csv')

# Extract the 'blood_glucose_level' column from each DataFrame
male_glucose = male_df['blood_glucose_level']
female_glucose = female_df['blood_glucose_level']

# getting proportions 
n1 = len(male_glucose)
n2 = len(female_glucose)

filtered_male = male_glucose[male_glucose < 120] 
filtered_female = female_glucose[female_glucose < 120] 

m1 = len(filtered_male)
m2 = len(filtered_female)

P1 = m1 / n1  
P2 = m2 / n2  

margin_of_error = abs(P1 - P2)
alpha = 0.05
beta = 0.20 

# ----------------------------------------------------------------
def calculate_sample_size(P1, P2, margin_of_error, alpha, beta):
    # Z-score corresponding to the desired confidence level
    z_a_tab = stats.norm.ppf(1 - alpha/2)
    z_b_tab = stats.norm.ppf(1 - beta)
    
    P = (P1 + P2) / 2
    Q = 1 - P
    
    z_val = (2 * (z_a_tab + z_b_tab)) ** 2

    # Calculate sample size using the formula
    required_sample_size = (z_val * P * Q) / (margin_of_error ** 2)

    return int(np.ceil(required_sample_size)//2)  # Round up to ensure a sufficient sample size

# ------------------------------------------------------------------
# calculations
estimated_sample_size = calculate_sample_size(P1, P2, margin_of_error, alpha, beta)

print("Estimated sample size for 2 samples = ", estimated_sample_size)