''' Assignment 3 Solutions '''

# Importing packages
from scipy.integrate import solve_ivp
import radioactivedecay as rd
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plt

# This wasn't in the Background Reading, but it is a nice way to set all the
# plot axis and label font face and font size at once
from matplotlib import rcParams
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 12

# Defining our known variables from the assignment, including the list of fluxes, abundance 
# of U-235 and yield of Sm-149
FLUX_list = [5e13, 1e14, 2e14]  # n/cm2 s
FLUX_list = [i* 3600 for i in FLUX_list] # n/cm2 h
abund_U235 = 0.719/100
YIELD_Sm149 = .0108 # fraction
# YIELD_I135 = 0.061
# YIELD_Xe135 = 0.003

# Defining our list of relevant isotopes and our fuel
iso_list = ['Pm-149', 'Sm-149']
fuel_iso = 'U-235'

# Some of the following functions are used to break up the overall decay functions
# into smaller parts, like fission_rate_U and burnup_rate.

# A function for determining the value of the production term for our isotope
def fission_rate_U(Flux_n):
    '''
    Uses properties of our isotope, in this case being U-235, and produces
    a production term.
    
    Args
    Flux_n: flux term
    
    Returns
    production_term: production rate, used later in decay_functs function
    '''
    nuc = rd.Nuclide(fuel_iso)
    sigma_f = 587 # barns
    sigma_f_cm2 = sigma_f * 10 ** (-24)
    
    N_atomic = 19.1 * NA * abund_U235 / nuc.atomic_mass
    
    macro_cross_f = sigma_f_cm2 * N_atomic
    
    production_term = Flux_n * macro_cross_f
    
    return production_term

# Defining a function for the burnup rate of our isotopes
def burnup_rate(Flux_n):
    '''
    Uses properties of our isotope to calculate a burnup rate.
    
    Args
    Flux_n: flux term
    
    Returns
    burnup_rate: the calculated burn up rate, used later in decay_functs function
    '''
    fuel_iso = iso_list[1]
    sigma_a = 41000 # b
    sigma_a_cm2 = sigma_a * 10 ** (-24)
    burnup_term = Flux_n * sigma_a_cm2
    
    return burnup_term

# Initial value of concentration and the decay constant of our isotopes. This function
# can be found in the background reading as well
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
    
    nuc = rd.Nuclide(iso)
    decay_const= np.log(2) / nuc.half_life('h') 
  
    if iso == iso_list[0]:
        input_atoms = 0
    else:
        input_atoms = 0     
    N_0_atoms = input_atoms
    
    return N_0_atoms, decay_const

# Decay functions function, which combines the previous functions to simplify
# the function from the background reading
def decay_functs(t, y, k1, FP_yield, Flux_n):
    '''
   Finds the decay functions for our input isotopes
   
   Args
    t: time, independent variable
    y: function, dependent variable
    k1: decay constant for parent
    FP_yield:
    Flux_n:
    
    Returns:
    dy: list of all right hand sides of coupled ODEs
    when set up as dy/dt = f(y, t)
    
    Right-hand side of all coupled ODE's when set up as dy/dt = f(y, t).
    This is used as input into the built-in ODE solver, solve_ivp. '''
    
    P1 = fission_rate_U(Flux_n) * FP_yield
    BurnUp = burnup_rate(Flux_n)
    dy0 = P1 - k1 * y[0]
    dy1 = k1 * y[0] - BurnUp * y[1]

    dy = [dy0, dy1]
    
    return dy

# Final function that, when used, will provide the solution and plots for our isotopes
def solutions_and_plots(iso_list, t_input, FP_yield):
    '''
    Takes the values we have previously defined and plots the solution
    
    Args
    iso_list: list of isotopes defined earlier in the code
    t_input: time of interest, input by user
    FP_yield: the relevant yield of our product
    
    Returns
    sol.sol(t_input)
    '''
    
    # Some blank lists for later appending
    overalltime_range = [0, 1000]
    initialvalues_y_0 = []
    prod_consump_terms = []

    # Create the time samples for the output of the ODE solver.
    # I use a large number of points, only because I want to make
    # a plot of the solution that looks nice.
    t_eval = []
    for i in range(0, 1000, 50):
        t_eval.append(i)
        
    t_eval = t_eval
    labels = []
    for iso in iso_list:
        initialvalues_y_0.append(initial_val_decay_const(iso)[0])
     
    prod_consump_terms.append(initial_val_decay_const(iso_list[0])[1])
    prod_consump_terms.append(FP_yield)
    
    # Plotting Information, along with determining how many isotopes we have
    colours_Sm = ['navy', 'mediumvioletred', 'lightcoral', 'lightgreen']
    colours2_Pm = ['blue', 'magenta', 'salmon', 'forestgreen']
    
    for colr, colr2, flux in zip(colours_Sm, colours2_Pm, FLUX_list):
        
        if flux == FLUX_list[0]:
            prod_consump_terms.append(flux)
        else:
            prod_consump_terms.pop()
            prod_consump_terms.append(flux)
        
        sol = solve_ivp(
            decay_functs, overalltime_range, initialvalues_y_0, t_eval=t_eval, 
            args=(prod_consump_terms), dense_output = True
            )
    
        if len(FLUX_list) > 1:
            if len(FLUX_list) == 2:
                labels.append(iso_list[0] + ' ' + str(flux) + 
                              ' n/(cm$^2$h)'
                              )
                labels.append(iso_list[1] + ' ' + str(flux) + 
                              ' n/(cm$^2$h)'
                              )
            
            else:
                labels.append(str(flux) + ' n/(cm$^2$h)')
        else:
            labels.append(iso_list[0])
            labels.append(iso_list[1])
            
        if len(FLUX_list) <= 2:
            plt.plot(
                t_eval, sol.y[0], color = colr2, linestyle ='-', marker = '.'
                )
        else:
            None
            
        # We always want to plot Sm-149 concentration
        plt.plot(t_eval, sol.y[1], color = colr, linestyle ='--', marker = '.')
        
    
    # Could instead call individually, but loop above is easier
    # plt.plot(t_eval, sol.y[0])
    # plt.plot(t_eval, sol.y[1])
    
    plt.xlabel('Time (h)', labelpad=8)
    if len(FLUX_list) == 2:
        plt.ylim(0, 1.8e17)
        plt.ylabel('Number of Atoms per cm$^3$', labelpad=8)
        ncols = 2
    else:
        plt.ylim(0, 8e16)
        plt.ylabel('Number of Atoms per cm$^3$', labelpad=8)
        ncols = 2
      
    plt.legend(
        labels, ncol=ncols, edgecolor='black', loc='upper center', fontsize=11
        )
    plt.tick_params(axis="both",direction="in")
    plt.show()
    # The following commented out line are for saving the plot, which is better to leave
    # as is until the code is good to go 
    # if len(FLUX_list) >= 2:
    #     plt.savefig('SmEqm_multiflux_2fluxes.png', dpi=300)
    # else:
    #     plt.savefig('SmEqm_singleflux.png', dpi=300)
    
    return sol.sol(t_input)

# Calling the plotting function with a specific time input to solve
solutions_and_plots(
    iso_list, t_input=168*3, FP_yield=YIELD_Sm149
    )