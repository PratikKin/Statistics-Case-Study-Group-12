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

# selecting random sample
sample_size = int(input("Give sample size for data: "))
new_df = df.sample(n=sample_size, random_state=1)

# selecting only specific columns from random sample
selected_columns = ['diabetes', 'heart_disease', 'hypertension']
selected_data = new_df[selected_columns]

# changing selected_data to array for ease of calculations
selected_array = selected_data.to_numpy()

# Calculate the number of ones and zeros separately for each column
ones_count = np.sum(selected_array == 1, axis=0)
zeros_count = np.sum(selected_array == 0, axis=0)

# Create a 2D array to store ones, zeros, and their sum
result_2d_array = np.column_stack((ones_count, zeros_count, ones_count + zeros_count))

# Calculate the sum of all columns for the last row
column_sums = result_2d_array.sum(axis=0)
result_2d_array = np.vstack((result_2d_array, column_sums))

# Create a DataFrame to display the results
result_df = pd.DataFrame(result_2d_array, columns=['Yes', 'No', 'Sum'], index=selected_columns + ['Total'])

# printing data stored for reference
print(result_df)

#--------------------------------------------------------------------------------------------

def Chi_Sq_Cal(habit_2d):
    output_shape = (habit_2d.shape[0] - 1, habit_2d.shape[1] - 1)
    A = np.zeros(output_shape)

    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            A[i, j] = habit_2d[i, -1] * habit_2d[-1, j] / habit_2d[-1, -1]
            
            
    sum_of_differences = 0
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            sum_of_differences += (((habit_2d[i, j] - A[i, j]) ** 2) / A[i, j])
            
    sum_of_rows_A = A.shape[0]
    sum_of_columns_A = A.shape[1]

    degree_of_freedom = (sum_of_columns_A-1) * (sum_of_rows_A-1) 
            
            
    return sum_of_differences, degree_of_freedom

#----------------------------------------------------------------------------

# getting calculated values
chi_sq_cal, dof = Chi_Sq_Cal(result_2d_array)

# getting tabulated values
alpha =  0.05
chi_sq_tab = stats.chi2.ppf(1 - alpha, dof)

# summarizing results
if(chi_sq_cal <= chi_sq_tab):
    print("Accept H0")
else:
    print("Reject H0")