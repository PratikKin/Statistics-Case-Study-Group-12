import numpy as np
import scipy.stats as stats
import pandas as pd
import os

for dirname, _, filenames in os.walk('../Diabetes'):
    for filename in filenames:
        os.path.join(dirname, filename)

df = pd.read_csv('../Diabetes/diabetes_prediction_dataset.csv')

sample_size = int(input("Give sample size : "))
random_sample = df.sample(n=sample_size, random_state=1)
habit_counts = random_sample["smoking_history"].value_counts()

### ---------------------------------------------------------

unique_habits = habit_counts.index.tolist()
habit_counts_values = habit_counts.tolist()

total_counts = sum(habit_counts_values)
mean = total_counts / len(habit_counts_values)

H0 = "This is a good fit"
H1 = "This is not a good fit"

print("Hypothesis : \n")
print("H0 : ", H0)
print("H0 : ", H1, "\n")

# Create a DataFrame to store the results with named columns
result_df = pd.DataFrame(data={'Smoking history': unique_habits, 'Number': habit_counts_values})

# Print the DataFrame without indices
print("Data: ")
print(result_df.to_string(index=False))

df = len(habit_counts_values) - 1
alpha = 0.05
chi_sq_tab = stats.chi2.ppf(1 - alpha, df)

### ------------------------------------------------------------
# Function
def GoodnessTest(habit_val, mean):
    sum_of_squared_differences = sum((count - mean) ** 2 for count in habit_val)
    chi_sq_cal = sum_of_squared_differences / mean
    return chi_sq_cal

### -------------------------------------------------------
chi_sq_cal = GoodnessTest(habit_counts_values, mean)

if chi_sq_cal <= chi_sq_tab:
    print("\nAccept H0")
else:
    print("\nReject H0")
