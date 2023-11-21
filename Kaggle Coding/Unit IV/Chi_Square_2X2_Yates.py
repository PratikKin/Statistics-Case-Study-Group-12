import numpy as np
import pandas as pd
import scipy.stats as stats
import os

for dirname, _, filenames in os.walk('../Dataset Used'):
    for filename in filenames:
        os.path.join(dirname, filename)
        
df = pd.read_csv('../Dataset Used/diabetes_prediction_dataset.csv')

sample_size = int(input("Give sample size for data: "))
new_df = df.sample(n=sample_size, random_state=1)
selected_columns = ['diabetes', 'heart_disease']
selected_data = new_df[selected_columns]

selected_array = selected_data.to_numpy()

ones_count = np.sum(selected_array == 1, axis=0)
zeros_count = np.sum(selected_array == 0, axis=0)

result_2d_array = np.column_stack((ones_count, zeros_count))

# ----------------------------------------------------------------------------------

def calculate_chi_square(observed):
    # Calculate the row and column sums
    row_sums = [sum(row) for row in observed]
    col_sums = [sum(col) for col in zip(*observed)]
    total = sum(row_sums)

    # Calculate the expected frequencies
    expected = []
    for i in range(2):
        expected_row = []
        for j in range(2):
            expected_value = (row_sums[i] * col_sums[j]) / total
            expected_row.append(expected_value)
        expected.append(expected_row)

    # Calculate the chi-square statistic
    chi2 = 0.0
    for i in range(2):
        for j in range(2):
            observed_value = observed[i][j]
            expected_value = expected[i][j]
            chi2 += ((abs(observed_value - expected_value) - 0.5) ** 2) / expected_value

    return chi2, expected

def yates_corrected_chi_square_test(observed):
    # Calculate the chi-square statistic and expected frequencies
    chi2, expected = calculate_chi_square(observed)

    # Calculate the degrees of freedom
    dof = 1

    # Calculate the p-value using the chi-square distribution
    p = 1.0

    if chi2 > 0:
        p = 1 - (0.5 * (chi2 ** 0.5))

    return chi2, p, dof, expected


# ------------------------------------------------------------------------------------------
chi2, p, dof, expected = yates_corrected_chi_square_test(result_2d_array)

# Print the results
print("Yates' corrected chi2 =", chi2)
print("Yates' corrected p-value =", p)
print("Yates' corrected dof =", dof)
print("Yates' corrected expected =", expected)

alpha = 0.05

if(p <= alpha):
    print("Reject H0")
else:
    print("Accept H0")