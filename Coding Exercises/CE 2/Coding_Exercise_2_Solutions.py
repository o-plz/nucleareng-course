''' Coding Exercise 2 Solutions'''

# Importing packages
import periodictable as pdt

# Assigning isotopes from periodictable to variables
U_238 = pdt.U[238]
He_4 = pdt.He[4]
Na_24 = pdt.Na[24]
Au_186 = pdt.Au[186]
Zr_79 = pdt.Zr[79]

# Periodictable has a function called .isotopes that allows us to 
# check what isotopes an element has
# print (pdt.Au.isotopes)
# print (pdt.Zr.isotopes)

# Defining the list of isotopes we will be using
iso_list = [U_238, He_4, Na_24, Au_186, Zr_79]

# Creating a function that takes inputs of A and Z, and returns the
# ratio of N to Z
def neutron_proton_ratio(A, Z):
    '''
    Calculates the ratio of N to Z, which indicates stability.
    
    Args: 
    A: atomic mass number (A =  Z + N)
    Z: proton/atomic number
    
    Return: returns ratio_N_to_Z
    '''
    # print (A, Z)
    N = A - Z 
    if Z <= 0:
        print (A, Z)
        print('invalid proton number')
        Z = 1
    else:
        None
        
    ratio_N_to_Z = round(N / Z, 2) 
    
    return ratio_N_to_Z

# Defining a stability function
def isotope_stability(iso):
    '''
    Calculates the likely stability of an isotope given its proton value, Z, and N/Z ratio.
    
    Args: 
    iso: a list of isotopes which the stability would be calculated for

    Return:
    stability: returns whether an isotope is likely stable or unstable
    N_over_Z: uses the neutron_proton_ratio function defined above to find 
    the ratio of neutrons to protons
    '''
    s = 'likely stable'
    us = 'likely unstable'
    firstNZ_limit = 1
    secondNZ_limit = 1.4
    Z = iso.number

    N_over_Z = neutron_proton_ratio(iso.isotope, iso.number)
    
    if Z <= 20:
        if N_over_Z <= firstNZ_limit:
            stability = s
        else:
            stability = us
    
    elif 20 < Z < 80:
        if N_over_Z < secondNZ_limit:
            stability = s
        else:
            stability = us
            
    elif Z >= 80:
        stability = us
        
    else:
        None
   
    return stability, N_over_Z

# Creating empty lists for appending
All_stabilities = []
All_N_Z = []

# A for loop that will be used to append the results of the previous
# function to the empty lists created above
for iso in iso_list:
    stblty, N_Z = isotope_stability(iso)    
    All_stabilities.append(stblty)
    All_N_Z.append(N_Z)

# Creating an empty list for appending
lengthall_lists = []

# Combining all the lists together under one variable
all_lists = [iso_list, All_stabilities, All_N_Z]

# Appending all the lists to the empty list
for eachlist in all_lists:
    lengthall_lists.append(len(eachlist))

# This section can be uncommented to check the list lengths to make sure
# they are all the same
# if lengthall_lists[0] == lengthall_lists[1] == lengthall_lists[2]:
#     None
# else:
#     print('not all lists are the same length, something went wrong')

# This print statement helps create a table to display the data found
print('Isotope', ' N/Z ', 'Stability')
for isotope, ratio, stability in zip(iso_list, All_N_Z, All_stabilities):
    print (isotope, '', ratio, '', stability) 


