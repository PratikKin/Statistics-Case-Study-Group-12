### For Z-test for two sample
"""
Group Number : 12
"""

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

print("Hypothesis => \n")

H0 = "U1 >= U2"
H1 = "U1 < U2"

print(H0+"\n"+H1)

#----------------------------------------------------------------------------------------------
# functions

#get the mean
def findMean(population):
    U = population.mean()
    return U

#get the error term
def findError(var1, var2, n1, n2):
    error = np.sqrt((var1/(n1-1)) + (var2/(n2-1)))
    return error

#get the Z tabulated value
def Z_tab(A_ci):
    z_tab = stats.norm.ppf(1 - A_ci/2)
    return z_tab

#calculate the Z value
def Z_cal(U1, U2, var1, var2, n1, n2, x_male, x_female):
    mean_diff = abs(U1-U2)

    x_diff = abs(x_female-x_male)    
    
    deno_error = findError(var1, var2, n1, n2)
    
    z_cal = (abs(x_diff - mean_diff))/deno_error    
        
    return z_cal

#Find confidence interval
def calcCI(var1, var2, n1, n2, x_male, x_female):
    x_diff = abs(x_female-x_male)
    error = findError(var1, var2, n1, n2)
    z_lower = x_diff - z_tab * error
    z_upper = x_diff + z_tab * error
    
    print("\nConfindence Interval\n",z_lower," <= U1 - U0 < ", z_upper)
    
# ------------------------------------------------------------------------------------------------
# implementation ->
    
U1 = findMean(male_glucose)
U2 = findMean(female_glucose)

# generating random samples from known population

n1 = int(input("Sampling size for male : "))
n2 = int(input("Sampling size for female : "))

random_sample1 = male_glucose.sample(n=n1, random_state=1)
random_sample2 = female_glucose.sample(n=n2, random_state=1)

var1 = np.var(male_glucose)
var2 = np.var(female_glucose)

x_male = findMean(random_sample1)
x_female = findMean(random_sample2)

# getting z calculated and tabulated values

z_cal=Z_cal(U1, U2, var1, var2, n1, n2, x_male, x_female)

z_tab = Z_tab(0.05)

# finalizing results
if z_cal <= z_tab:
    print("Accept H0")
else:
    print("Reject H0")
    
# printing Confidence Interval
    
calcCI(var1, var2, n1, n2, x_male, x_female)