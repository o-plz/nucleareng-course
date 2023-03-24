''' Background Reading 3'''

# Importing packages
from scipy.integrate import solve_ivp
from scipy.constants import Avogadro as NA
import numpy as np
import radioactivedecay as rd
import matplotlib.pyplot as plt


''' General Numpy Information'''

# Using np.log10 to take the log base 10 of array and single input
A = [1, 2, 3]
# print(np.log10(A))
B = 4
# print(np.log10(B))

''' Radioactivedecay Package '''

# The following lines will show some of the capability of 
# the radioactivedecay package
# Creating a nuclide 
nuc_I135 = rd.Nuclide('I-135')

# Obtaining the half-life
I135_halflife = nuc_I135.half_life('s')
# print (I135_halflife)

# Using the half-life obtained to find the decay constant
I135_decayconst = 0.693 / I135_halflife

# Obtaining the next decay product
next_daughter_135 = nuc_I135.progeny()

# Another way to get next decay product, e.g., for U-235
# This is helpful if you didn't already specify a variable 
# for the isotope you're interested in
next_daughter_U235 = rd.Nuclide('I-135').progeny()

# Some print statements to show some of the things we've found
# print(I135_decayconst)
# print(next_daughter_I135)
# print (next_daughter_U235)

# Initial amount of parent isotope at t = 0
# Here, the isotope and it's initial weight must be specified, 
# as well as the units of mass
inv_mass_t0 = rd.Inventory({'I-135': 10.0}, 'g')

# This next line shows the the new inventory after decay takes place for 
# the specified amount of time, which in this case is 26.3 hours. It uses
# the inventory found in the last line
inv_mass_t1 = inv_mass_t0.decay(26.3, 'h')

# Obtaining the masses of decay products
# The mass units required can be specified
masses_progeny = inv_mass_t1.masses('g')

# If 'mol' inside brackets below is left out, the default is moles, since this uses
# .moles() method, but it's still good practice to specify for clarity when quickly 
# looking at code later
moles_progeny = inv_mass_t1.moles('mol')

# Prints all daughters (listed alphabetically)
print (
    'amounts of all daughters in units specified when masses_progeny made: \n', 
    masses_progeny)

print()

# Prints only selected daughters, using square bracket 'X-A' notation
print (
    'moles Ba-135: ', moles_progeny['Ba-135'], 
    '# atoms Ba-135:',  inv_mass_t1.numbers()['Ba-135'], '\n',
    'activity I-135 in Mega Curies:', inv_mass_t1.activities('MCi')['I-135']
    )

# We can also look at the order of daughter products graphically 
# This can be uncommented to look at the graph
# nuc_I135.plot()
# plt.show()

# If nuc_I135 was not previously defined, the following could be used:
# rd.Nuclide('I-135').plot()
# inv_mass_t0.plot(100, 'h')
# plt.show()

''' ODE solver '''

# Defining our isotopes
iso_list = ['I-135', 'Xe-135']

# Creating a function that will find the decay functions
# for the listed isotopes
def decay_functs(t, y, k1, k2): 
    '''
    Args:
    t: independent variable
    y: dependent variable
    k1: decay constant for parent
    k2: decay constant for first daughter
    
    Returns:
    dy: list of all right hand sides of coupled ODEs
    when set up as dy/dt = f(y, t)
    
    Right-hand side of all coupled ODE's when set up as dy/dt = f(y, t).
    This is used as input into the built-in ODE solver, solve_ivp.
    '''
    # Decay only ODE, production = 0
    # Units for y dictated by initial input
    # E.g., if y_0 is atoms, y = [atoms]
    dy0 = -k1 * y[0]
    dy1 = k1 * y[0] -  k2 * y[1]
    dy = [dy0, dy1]
    
    return dy

# Creating a function that will find the decay constants and initial
# amounts of the isoptopes listed
def initial_val_decay_const(iso):
    '''
    Determines the decay constant and initial amount of a specified isotope
    
    Args:
    iso: input isotope in 'X-A' string format, where X is the element symbol
    and A is the atomic mass number. This input is used in radioactivedecay 
    package inside this function
    
    Returns:
    N_0_atoms: initial concentration of isotope, in atoms
    decay_const: calculated from half-lives, which are found using the 
    radioactivedecy package inside this function
    '''
    # This first line assigns the isotope input to a variable for 
    # easy of use
    nuc = rd.Nuclide(iso)
    
    # log10 is base ten, log is natural log (ln)
    decay_const= np.log(2) / nuc.half_life('h') 
    
    # This for loop is used to assign an initial mass for an isotope
    # In this case, it is the first isotope in our list, with the rest
    # having an initial concentration of 0
    if iso == iso_list[0]:
        input_g = 10
        nuc_MW = nuc.atomic_mass
        N_0_atoms = NA * input_g / nuc_MW
        
    else:
        N_0_atoms = 0     
    
    return N_0_atoms, decay_const

# Assigning empty lists
initialvalues_y_0 = []
k = []

# Using the functions created to find the initial concentrations and the
# decay constants of our isotopes, then appending to our empty lists    
for iso in iso_list:
    k.append(initial_val_decay_const(iso)[1])
    initialvalues_y_0.append(initial_val_decay_const(iso)[0])

# Defining the range of our solver    
overalltime_range = [0, 80]

# This for loop appends a list of time values to be used in our solver
t_solutions = [] 
for i in range(0, 80, 2):
    t_solutions.append(i)
    
# Defining our IVP solver, using values we've previously found
sol = solve_ivp(
        decay_functs, overalltime_range, initialvalues_y_0, t_eval= t_solutions, 
        args=(k), dense_output = True
        )

# These print statements can be uncommented to view specific values
# print('solution to first ODE, I-135:', sol.y[0])
# print ('')
# print('t-values ODEs solved at:', sol.t)    

# This section of code allows us to solve for specific t values using
# t_input
t_input = 40
specific_sol = sol.sol(t_input)
print (specific_sol)

''' Plotting solution to system of ODEs below '''

# These colors can be changed to your liking, full lists of colors
# can be found online
plotcolours = ['mediumseagreen', 'mediumorchid']

# This for loops defines what our variables will look like when plotted
# It's not necessary to do this to make the plots, but it is more
# convenient then having to declare a bunch of variables for just the 
# I-135 y vals, then the Xe-135 vals (and so on, for a larger system of ODEs) 
for solution, colr in zip(sol.y, plotcolours):
    # plot function takes (x point list, y point list)
    plt.plot(sol.t, solution, color = colr, linestyle ='-', marker = '.')


# Information provided on font style, this is in "dictionary" style
# We have not learned about dictionaries yet, but the defining 
# of font properties using keywords below is easy to follow
font = {'family': 'arial',
    'color':  'black',
    'weight': 'normal',
    'size': 12,
    }


# First argument is the string name of the label, second argument is the font info,
# third argument is the desired padding space between the axis values and the 
# label location
plt.xlabel('Time (h)', fontdict = font, labelpad=8)
plt.ylabel('Number of Atoms', fontdict=font, labelpad=8) 
     
labels = iso_list

# Labels are the string names of the different curves
# ncol is how many columns we want the legend labels to be in
# edgecolor is the colour of the legend box
# loc is the location of the legend
plt.legend(labels, ncol=1, edgecolor='black', loc='upper right', fontsize=10)

# Turns tickmarks inward
plt.tick_params(axis="both",direction="in", labelsize = '12')

# This next line shows plot, which is useful when tweaking so you don't have to 
# keep opening the saved file. Comment out the plt.show when you are happy with 
# the plot and ready to save the figure 
# plt.show()

# This last line saves figure with the string name.extension of filetype you would like 
# as the first argument... dpi is the resolution (300 or 400 dpi is good)
# Figure is saved to your local Git repository folder by default
# plt.savefig('I-135_activiy.png', dpi=300)

