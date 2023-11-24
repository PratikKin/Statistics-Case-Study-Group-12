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

# getting random sample
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
# functions
def Chi_Sq_2X2(total_sum, resultantArray):
    a = resultantArray[0, 0]
    b = resultantArray[0, 1]
    c = resultantArray[1, 0]
    d = resultantArray[1, 1]
    
    deno = (a+b) * (c+d) * (a+c) * (b+d)
    numerator = total_sum*((abs(a*d-b*c) - total_sum/2)**2)
    
    cal = numerator/ deno
    return cal
    

# -----------------------------------------------------------------------
# Calculations
# getting calculated and tabulated values


a = result_2d_array[0, 0]
b = result_2d_array[0, 1]
c = result_2d_array[1, 0]
d = result_2d_array[1, 1]
    
e11 = (a+b)*(a+c)/(a+b+c+d)
e12 = (a+b)*(b+d)/(a+b+c+d)
e21 = (c+d)*(a+c)/(a+b+c+d)
e22 = (c+d)*(b+d)/(a+b+c+d)

print(result_2d_array)
    
# we can only proceed if any one of the expected cell frequencies is less than 5
if(e11 < 5 or e12 < 5 or e21 < 5 or e22 < 5):
    
    # Hypothesis
    print("Hypothesis : \nH0 : There is no relationship between Diabetes and Heart Disease.\nH1 : There is a relationship between Diabetes and Heart Disease.")

    chi_sq_cal = Chi_Sq_2X2(N, result_2d_array)

    alpha = 0.05
    chi_sq_tab = stats.chi2.ppf(1-alpha, 1)

    # summarizing results
    if(chi_sq_cal <= chi_sq_tab):
        print("Accept H0")
    else:
        print("Reject H0")
else:
    print("Cannot go with 2X2 Contingency test with Yate's correction! \nGo with 2X2 Contingenct Test!")