### t-test for double mean small sample
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

H0 = "U1 >= U2"
H1 = "U1 < U2"
# One tailed test

print(H0+"\n"+H1)

#----------------------------------------------------------------------------------------------
# functions

#get the mean
def findMean(population):
    U = population.mean()
    return U

#find the error term
def findError(var1, var2, n1, n2):
    sum_sp = (n1-1)*var1 + (n2-1)*var2
    deno_sp = n1+n2-2
    sp = sum_sp/deno_sp
    sum_n = (1/n1) + (1/n2)
    error = np.sqrt(sp * sum_n) 
    return error

#get the t-tabulated value
def T_tab(alpha, df, two_tailed=True):
    if two_tailed:
        alpha /= 2  # For a two-tailed test, divide alpha by 2

    t_tab = stats.t.ppf(1 - alpha, df)

    return t_tab

#calculate t-value
def t_cal(U1, U2, var1, var2, n1, n2, x_male, x_female):
    mean_diff = abs(U1-U2)
    deno_error = findError(var1, var2, n1, n2)
    x_diff = abs(x_female-x_male)    
    t_cal = (abs(x_diff - mean_diff))/deno_error    
    
    return t_cal

#calculate the confidence interval
def calcCI(var1, var2, n1, n2, x_male, x_female):
    x_diff = abs(x_female-x_male)
    error = findError(var1, var2, n1, n2)
    t_lower = x_diff - t_tab * error
    t_upper = x_diff + t_tab * error
    
    print("Confindence Interval\n",t_lower," <= |U1 - U0| < ", t_upper)
    
#-------------------------------------------------------------------------------
# application

U1 = findMean(male_glucose)
U2 = findMean(female_glucose)

# getting samples from actual population
n1 = int(input("Sampling size for male : "))
n2 = int(input("Sampling size for female : "))

random_sample1 = male_glucose.sample(n=n1, random_state=1)
random_sample2 = female_glucose.sample(n=n2, random_state=1)

var1 = np.var(male_glucose)
var2 = np.var(female_glucose)

x_male = findMean(random_sample1)       #mean for the sample of male
x_female = findMean(random_sample2)     #mean for the sample of female

# getting t tabulated and calculated values
t_cal=t_cal(U1, U2, var1, var2, n1, n2, x_male, x_female)

t_tab = T_tab(0.05, n1+n2-2, False)

# summarizing results
if n1 < 30 and n2 < 30:
    if t_cal >= t_tab:
        print("Accept H0")
    else:
        print("Reject H0")
    
    # getting confidence interval
    calcCI(var1, var2, n1, n2, x_male, x_female)
else :
    print("Unable to compute")
    
