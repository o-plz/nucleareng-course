''' Assignment 1 Coding Portion Solutions
    Option #2: Periodictable Package Approach'''
# While optional, this method allows students the chance to try out using
# imported packages. 

# Importing necessary packages
import periodictable as pdt

# Defining known variables for the SEMF equation
a_v = 15.73
a_s = 17.84
a_c = 0.7103
a_A = 23.69
a_p = 33.6

# Isotope list using periodictable package, which follows the format 
# pdt.element[isotope number], with pdt being whatever you called the 
# package    
list_isotopes = [
    pdt.H[1], pdt.He[3], pdt.He[4], pdt.Li[6], pdt.C[12], pdt.C[14], 
    pdt.S[40], pdt.Ca[40], pdt.Pu[240]
    ]

# Empty list for later appending
all_BEs = [] 

# Defining a function for use in calculating the BE for each nucleus
for isotope in list_isotopes:

# A and Z are our input parameters, which were defined by us in option
# 1, while here pdt is used to recall them
    A = isotope.isotope
    Z = isotope.number

    vol_term = a_v * A 
    surface_term = a_s * (A ** (2/3))
    coulomb_term = a_c * (Z ** 2) / (A ** (1/3))
    asymmetry_term = (a_A * (A - 2 * Z) ** 2) / A
    pairing_term = ((-1) ** Z) * a_p  * (1 + (-1) ** A) / (2 * A ** (3/4))

    BE = vol_term - surface_term - coulomb_term - asymmetry_term + pairing_term

    BE_per_nucleon = round(BE / A, 3)

    all_BEs.append(BE_per_nucleon)
    
# Creating a list for the BE values obtained using the Chart of the Nuclides to compare
# to the calculated BE from the SEMF equation
BEs_ChartNuclides = [
    0, 2.572681, 7.073915, 5.332331, 7.680144, 7.520319, 8.329325, 8.551304,
    7.556035
    ]

# Creating a print statement to display the data found
print ('Isotope','BE/A ', 'BE/A (LDM)', '% error')
print ('        ',   'MeV', '    ',   'MeV')
for i, j, k in zip (list_isotopes, BEs_ChartNuclides, all_BEs):
    print (i, ' ', j, '  ', k, '  ', round(100 * abs(j - k) / k, 3))
