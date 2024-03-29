''' Assignment 1 Coding Portion Solutions
    Option #1: Traditional List Approach ''' 
# This option makes lists of input parameters that correspond to each of the chosen isotopes
# that are later used in a function to calculate BE using the SEMF equation.

# Creating isotope list
list_isotopes = ['H-1', 'He-3', 'He-4', 'Li-6', 'C-12', 'C-14', 'Ca-40', 'Co-59', 'Pu-240']

# Creating input parameter lists
mass_numbers = [1, 3, 4, 6, 12, 14, 40, 40, 240]
proton_numbers = [1, 2, 2, 3, 6, 6, 16, 20, 94]

# Defining known variables for the SEMF equation
a_v = 15.73
a_s = 17.84
a_c = 0.7103
a_A = 23.69
a_p = 33.6

# Empty list for later appending
all_BEs = [] 

# Creating a loop that will go through our input variables and calculate the BE for 
# each nucleus. These values are then appended to our empty list
for Z, A, in zip(proton_numbers, mass_numbers):
    
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

