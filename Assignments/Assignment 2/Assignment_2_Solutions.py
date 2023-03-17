''' Assignment 2 Solutions'''

# Importing packages
from scipy.constants.constants import Avogadro
import numpy as np
import math

# Half lives are found using the Chart of the Nuclides and need to be 
# in seconds, so they are first converted
t_halfB = 1.91 * 3600
t_halfC = 6.646 * 24 * 3600

# Combining the above half lives into a list and creating an empty list
all_thalf = [t_halfB, t_halfC]
all_lambdas = []

# For loop that finds the lambda value from the half lives found
for i in all_thalf:
    lambd =  math.log(2) / i
    all_lambdas.append(lambd)

# Creating individual values for each lambda value    
lambdaB, lambdaC = all_lambdas
# print (lambdaB, lambdaC)

# Defining the variables needed to calculate the concentration of Yb-176
P = 5.7e-9 # atoms/s
mass_Yb176 = 100 # g
MW_Yb176 = 175.942576447 # g/mol
abundanceYb_176 = 12.996 / 100 # fractional
# g --> mol --> atoms
N_Yb176 = (mass_Yb176 / MW_Yb176) * Avogadro

# print (N_Yb176) 

# Creating a function to calculate the Lu-177 concentration
def Lu_conc_calculator(time_h):
    '''
    Calculates the concentration of Lu-177 as a function of time.
    Analytical solution equation is given in assignment question.
    
    Args:
    time_h: time, integer, in hours
    
    Return: 
    N_C: concentration of Lu-177, float, in atoms
    
    '''
    # As before, half life is in seconds so time needs to be converted
    time_s = time_h * 3600
    
    # Breaking up separate parts of the equation for easier handling
    pre_exp = P * N_Yb176 * lambdaB
    
    exp1_num = np.exp(-P*time_s)
    exp1_denom = (lambdaB - P) * (lambdaC - P)
    
    exp2_num = np.exp(-lambdaB * time_s)
    exp2_denom = (P - lambdaB) * (lambdaC - lambdaB)
    
    exp3_num = np.exp(-lambdaC * time_s)
    exp3_denom = (P - lambdaC) * (lambdaB - lambdaC)
    
    N_C = pre_exp * (
        (exp1_num / exp1_denom) 
        + (exp2_num / exp2_denom) 
        + (exp3_num / exp3_denom)
        )
    
    return N_C

# sat_atoms is the maximum amount of Lu-177 atoms, which can be found by 
# students a few ways
sat_atoms = 1.57535e+21
sat_90_percent = sat_atoms * 0.90 

# Time loop range to find max, this can be adjusted to find the right
# range, all in hours:
start = 500
stop = 1500 
step = 48 

# Using the above time parameters to find the concentration of Lu-177
# at 90% saturation and the time required to reach it
for t in range(start,stop,step): # hours
    N_Lu177 = Lu_conc_calculator(t)
    # print (t, N_Lu177)
    # if statement that allows a range on N_Lu177 values around 90%
    if sat_atoms * 0.895 <= N_Lu177 <= sat_atoms * 0.905:
        print (
            "Number of weeks: ", round(t / 24 / 7, 2), ',',
            'Atoms of Lu-177 at 90% saturation: ', N_Lu177
            )
        break
    else:
        None

# Activity check (should be around ~ 400 Ci/g Yb176)
activity_Lu177 = N_Lu177 * lambdaC # Bq
activity_Lu177 = activity_Lu177 / (3.7 * 10 ** 10)
activity_Lu177_g_Yb = activity_Lu177 / mass_Yb176

# print (round(activity_Lu177_g_Yb, 3), 'Ci/g Yb176 or mCi/mg Yb176')