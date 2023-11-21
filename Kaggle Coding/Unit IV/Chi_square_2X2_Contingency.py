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


#----------------------------------------------------------------
def chi_square_test(observed):
    row_totals = [sum(row) for row in observed]
    col_totals = [sum(col) for col in zip(*observed)]

    grand_total = sum(row_totals)

    expected = [[(row_total * col_total) / grand_total for col_total in col_totals] for row_total in row_totals]

    chi2 = sum([(observed[i][j] - expected[i][j]) ** 2 / expected[i][j] for i in range(len(observed)) for j in range(len(observed[0]))])

    dof = (len(observed) - 1) * (len(observed[0]) - 1)

    p = stats.chi2.cdf(chi2, dof)
    return chi2, p, dof, expected

# 8------------------------------------------------------------------------------
chi_sq_cal, p, dof, expected = chi_square_test(result_2d_array)

# Print the results
print("chi2 =", chi_sq_cal)
print("p-value =", p)
print("dof =", dof)
print("expected =", expected)

alpha = 0.05

if(p <= alpha):
    print("Reject H0")
else:
    print("Accept H0")