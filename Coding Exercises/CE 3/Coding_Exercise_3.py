''' Coding Exercise 3 '''

# Importing packages
from scipy.integrate import solve_ivp
import radioactivedecay as rd
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plt
from matplotlib import rcParams

# This wasn't in the Background Reading, but is a nice way to set all the
# plot axis and label font face and font size all in one fell swoop
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 12

# Identifying R, which is the rate of production given in assignment 2
R_sec = 5.7e-9  #s-1
R_hour = R_sec * 3600 #h-1 

# Creating a list of the isotopes we're interested in
iso_list = ['Yb-176', 'Yb-177', 'Lu-177']

# Defining a function that converts the amount of our isotopes to atoms
def atoms_converter(input_g, iso):
    '''
    Converts amount of isotope from grams to atoms
    Args
    input_g: amount of isotope in grams
    iso: isotope identifier, using notation from radioactivedecay package,
    e.g., "X-A", where X is the element's symbol, and A is the atomic mass #
    
    Returns
    input_atoms: amount of input isotope, but converted to atoms
    '''
    # Converts mass input to atoms
    nuc_MW = rd.Nuclide(iso).atomic_mass
    input_atoms = NA * input_g / nuc_MW
    
    return input_atoms

# Defining a function that determines the initial amounts of the isotopes present
# and the decay constants of these isotopes
def initial_val_decay_const(iso):
    '''
    Setup for all initial amounts of isotopes in system, which are combined
    into a list and appends decay constants of all decaying species into list
    
    Args
    iso: isotope identifier from radioactivedecay package
    
    Returns
    N_0_atoms: initial amounts of all isotopes in system of ODEs to be solved
    decay_const: decay constants of all isotopes 
    
    '''
    # Defining a variable that corresponds to our isotope from the 
    # radioactivedecay package
    nuc = rd.Nuclide(iso)
    
    # Based on input isotope (iso), calcuates decay constant using half life
    # log10 is base ten, log is natural log (ln)
    decay_const= np.log(2) / nuc.half_life('h') 
    
    # Using an if statement, we can assign our parents isotope to have a specific 
    # initial value, while the others are assigned to have no initial value
    if iso == iso_list[0]:
        input_g = 100
    else:
        input_g = 0    
        
    # Lastly, the concentration of our isotopes can be found using the 
    # atoms_converter function we defined earlier, using the grams we just
    # assigned and the isotope that it corresponds to 
    N_0_atoms = atoms_converter(input_g, iso)
    
    return N_0_atoms, decay_const
    
# Defining a function that sets up our ODE functions, dy
def decay_functs(t, y, k1=None, k2=None, k3=None): 
    '''
    Sets up the system of ODEs to be solved, using notation 
    dy/dt = material balance, where only the RHS for each of 
    y0, y1, y2,... yn are needed
    
    Args
    t: time, independent variable
    y: dependent variable 
    k1, k2, k3 = coefficients (not variable with time, here these are 
    our decay constants) for each of the isotopes 
    
    Returns
    dy: set up for use in solve_ivp function specifically, following its notation
    '''
    
    # If decay only ODE, production = 0
    # Units for y is dictated by initial input
    # E.g., if y_0 is atoms, y = [atoms]
    # y0 consumed by neutron activation to form y1
    dy0 = -R_hour * y[0]
    
    # y1 produced from neutron activation of y0 and consumed by y1 decay
    dy1 = R_hour * y[0] -  k2 * y[1]
    
    # y2 produced from decay of y1 and consumed by y2 decay
    dy2 = k2 * y[1] -  k3 * y[2]
    
    # This code safeguards in case this function is used only for parent decay
    if len(iso_list) < 2:
        dy = dy0
    elif len(iso_list) < 3:
        dy = [dy0, dy1]
    # This is also assuming for now that only max 3 coupled ODEs need solving
    else:
        dy = [dy0, dy1, dy2]
    return dy

# Next, a function is defined to solve the ODE, using the isotope list and an input time
def ODE_solutions(iso_list, t_input):
    '''
    Uses solve_ivp solver to calculate solutions to ODE system
    and to plot output 
    
    Args
    iso_list: list of all isotopes that need to be solved for
    t_input: time increments at which numerical solution will be interpolated at
    
    Return
    sol.sol(t_input) = solution to ODE system at specific time (see t_input in 
    Args above)
    '''
    
    overalltime_range = [0, 1000]
    initialvalues_y_0 = []
    k = []

    # Create the time samples for the output of the ODE solver.
    # A large number of points is used here because the solutions will be plotted
    # and more points results in a nicer looking plot
    t_eval = []
    for i in range(0,1000,50):
        t_eval.append(i)
        
    t_eval = t_eval
    
    # Appending our solved values to the blank lists
    for iso in iso_list:
        k.append(initial_val_decay_const(iso)[1])
        initialvalues_y_0.append(initial_val_decay_const(iso)[0])
    
    # Next is the main solver portion. Dense_output set to "True", to allow us to 
    # interpolate solution at desired input (even if this isn't one of the time  
    # intervals that the RK4 numerically solved the system of ODEs at)
    sol = solve_ivp(
        decay_functs, overalltime_range, initialvalues_y_0, t_eval=t_eval, 
        args=(k), dense_output = True
        )
    
    # Creating our plot
    colours = ['navy', 'mediumvioletred', 'lightcoral']
    for solution, colr in zip(sol.y, colours):
        plt.plot(
            t_eval, solution, color = colr, linestyle ='-', marker = '.'
            )
    plt.ylim([1.25e17, 4e24])
    
    plt.yscale('log')
   
    labels = iso_list
    
    plt.xlabel('Time (h)', labelpad=8)
    plt.ylabel('Number of Atoms', labelpad=8)
    plt.legend(labels, ncol=1, edgecolor='black', loc='lower right')
    plt.tick_params(axis="both",direction="in")
    plt.show()
    # This next line can be uncommented to save the figure
    # plt.savefig('Po-218_Decay_OP.png', dpi=300)
    
    return sol.sol(t_input)

# The following is another method for the print statement, using a specific time 
# setting provided by us. The print statement itself can be uncommented to show
num_days = 21
num_hours = num_days * 24

# Simplified print statement:
# print (ODE_solutions(iso_list, t_input=num_hours))
# Or, a nicer print statement:
####  print (i, ":", j)
    