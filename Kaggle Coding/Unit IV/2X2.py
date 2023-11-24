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

### -------------------------------------------------------------------

# selecting random sample
sample_size = int(input("Give sample size for data: "))
new_df = df.sample(n=sample_size, random_state=1)

# selecting only specific columns from random sample
selected_columns = ['diabetes', 'heart_disease']
selected_data = new_df[selected_columns]

# changing selected_data to array for ease of calculations
selected_array = selected_data.to_numpy()

# getting counts of 1 (true or yes) and 0 (false or no)
ones_count = np.sum(selected_array == 1, axis=0)
zeros_count = np.sum(selected_array == 0, axis=0)

# adding the column names, their respective values of 1's and 0's
result_2d_array = np.column_stack((ones_count, zeros_count))

# N = sum of all elements (a+b+c+d) in [[a, b], [c, d]]
N = np.sum(result_2d_array)

# ----------------------------------------------------------------------

def Chi_Sq_2X2(total_sum, resultantArray):
    a = resultantArray[0, 0]
    b = resultantArray[0, 1]
    c = resultantArray[1, 0]
    d = resultantArray[1, 1]

    cal = ((total_sum * (a * d - b * c)**2) / ((a + b) * (b + d) * (a + c) * (c + d)))
    return cal

# -----------------------------------------------------------------------
# Calculations

# getting calculated values
chi_sq_cal = Chi_Sq_2X2(N, result_2d_array)

# getting tabulated values
alpha = 0.05
chi_sq_tab = stats.chi2.ppf(1-alpha, 1)

print(result_2d_array)

# summarizing results
if(chi_sq_cal <= chi_sq_tab):
    print("Accept H0")
else:
    print("Reject H0")
