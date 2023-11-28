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

# getting  random samples
male_sample_size = int(input("Give sample size for male data: "))
male_random_sample = male_df.sample(n=male_sample_size, random_state=1)

female_sample_size = int(input("Give sample size for female data: "))
female_random_sample = female_df.sample(n=female_sample_size, random_state=1)

# getting counts of members available
male_habit_counts = male_random_sample["smoking_history"].value_counts()
female_habit_counts = female_random_sample["smoking_history"].value_counts()

### --------------------------------------------
# taking only unique entities with their respective counts
unique_habits = male_habit_counts.index.tolist()

habit_counts_2d_array = np.column_stack((male_habit_counts.values, female_habit_counts.values))

sum_of_columns = np.sum(habit_counts_2d_array, axis=1, keepdims=True)
habit_counts_2d_array = np.column_stack((habit_counts_2d_array, sum_of_columns))

sum_of_rows = np.sum(habit_counts_2d_array, axis=0, keepdims=True)
habit_counts_2d_array = np.vstack((habit_counts_2d_array, sum_of_rows))

# --------------------------------------------------------------------------
# functions

def Chi_Sq_Cal(habit_2d):
    output_matrix = (habit_2d.shape[0] - 1, habit_2d.shape[1] - 1)
    ExpectedMatrix = np.zeros(output_matrix)     ### Expected matrix is the matrix formed with the expected values associated with the output matrix 

    for i in range(output_matrix[0]):
        for j in range(output_matrix[1]):
            ExpectedMatrix[i, j] = habit_2d[i, -1] * habit_2d[-1, j] / habit_2d[-1, -1]

    # Calculate the sum of (square of differences of values of O[i, j] and A[i, j]) divided by A[i, j]
    sum_of_differences = 0
    for i in range(output_matrix[0]):
        for j in range(output_matrix[1]):
            sum_of_differences += (((habit_2d[i, j] - ExpectedMatrix[i, j]) ** 2) / ExpectedMatrix[i, j])
            
    sum_of_rows_ExpectedMatrix = ExpectedMatrix.shape[0]
    sum_of_columns_ExpectedMatrix = ExpectedMatrix.shape[1]

    degree_of_freedom = (sum_of_columns_ExpectedMatrix-1) * (sum_of_rows_ExpectedMatrix-1)
            
    return sum_of_differences, degree_of_freedom


#-------------------------------------------------------------------------

# stating Hypothesis
print("Hypothesis: \nH0 : People have disease independent of their gender.\nH1 : People don't have disease independent of their gender.")

# getting calculated and tabulated values
chi_sq_cal, dof = Chi_Sq_Cal(habit_counts_2d_array)

alpha =  0.05
chi_sq_tab = stats.chi2.ppf(1 - alpha, dof)

print(habit_counts_2d_array)
print("Chi Square Calculated = ", chi_sq_cal)
print("Chi Square Tabulated = ", chi_sq_tab)

# summarizing results
if(chi_sq_cal <= chi_sq_tab):
    print("Accept H0")
else:
    print("Reject H0")

