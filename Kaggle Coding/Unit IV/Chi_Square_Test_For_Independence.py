import numpy as np
import pandas as pd
import scipy.stats as stats
import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        os.path.join(dirname, filename)

male_df = pd.read_csv('../Dataset Used/male_glu.csv')
female_df = pd.read_csv('../Dataset Used/female_glu.csv')

male_sample_size = int(input("Give sample size for male data: "))
male_random_sample = male_df.sample(n=male_sample_size, random_state=1)

female_sample_size = int(input("Give sample size for female data: "))
female_random_sample = female_df.sample(n=female_sample_size, random_state=1)

male_habit_counts = male_random_sample["smoking_history"].value_counts()
female_habit_counts = female_random_sample["smoking_history"].value_counts()

### --------------------------------------------
unique_habits = male_habit_counts.index.tolist()

habit_counts_2d_array = np.column_stack((male_habit_counts.values, female_habit_counts.values))

sum_of_columns = np.sum(habit_counts_2d_array, axis=1, keepdims=True)
habit_counts_2d_array = np.column_stack((habit_counts_2d_array, sum_of_columns))

sum_of_rows = np.sum(habit_counts_2d_array, axis=0, keepdims=True)
habit_counts_2d_array = np.vstack((habit_counts_2d_array, sum_of_rows))

# Define the shape of the output matrix A

def Chi_Sq_Cal(habit_2d):
    output_shape = (habit_2d.shape[0] - 1, habit_2d.shape[1] - 1)
    A = np.zeros(output_shape)

    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            A[i, j] = habit_2d[i, -1] * habit_2d[-1, j] / habit_2d[-1, -1]

# Calculate the sum of (square of differences of values of O[i, j] and A[i, j]) divided by A[i, j]
    sum_of_differences = 0
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            sum_of_differences += (((habit_2d[i, j] - A[i, j]) ** 2) / A[i, j])
            
    sum_of_rows_A = A.shape[0]
    sum_of_columns_A = A.shape[1]

    degree_of_freedom = (sum_of_columns_A-1) * (sum_of_rows_A-1)
            
    return sum_of_differences, degree_of_freedom


#-------------------------------------------------------------------------

H0 = "This is Independent"
H1 = "This is not Independent"

print("Hypothesis : \n")
print(H0)
print(H1, "\n")


chi_sq_cal, dof = Chi_Sq_Cal(habit_counts_2d_array)

alpha =  0.05
chi_sq_tab = stats.chi2.ppf(1 - alpha, dof)

print("Chi Square Calculated = ", chi_sq_cal)
print("Chi Square Tabulated = ", chi_sq_tab)

if(chi_sq_cal <= chi_sq_tab):
    print("Accept H0")
else:
    print("Reject H0")
    
print(habit_counts_2d_array)