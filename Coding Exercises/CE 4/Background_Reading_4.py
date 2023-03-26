''' Background Reading 4 '''

# Importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator

rcParams['font.family'] = 'arial'
rcParams['font.size'] = 12

# Defining our known parameters
DIFFUSION_COEFF_D2O = 0.87 # cm
DIFFUSION_COEFF_H2O = 0.16 # cm
SOURCE = 10** 7 # n/s
DIFFUSION_LENGTH_D2O = 97 # cm
DIFFUSION_LENGTH_H2O = 2.85 # cm

# Setting our moderator, and creating an if/else statement to check which
# moderator is stated
Moderator = 'H2O'

if Moderator == 'H2O':
    DIFFUSION_LENGTH = DIFFUSION_LENGTH_H2O
    DIFFUSION_COEFF = DIFFUSION_COEFF_H2O
else:
    DIFFUSION_LENGTH = DIFFUSION_LENGTH_D2O
    DIFFUSION_COEFF = DIFFUSION_COEFF_D2O

''' Function to calculate infinite slab source flux ''' 
    
def flux_inf_planr_source(x):
    
    ExponentialTerm = np.exp(-abs(x) / DIFFUSION_LENGTH)
    Flux = SOURCE * DIFFUSION_LENGTH * ExponentialTerm / (2 * DIFFUSION_COEFF)
    
    return Flux
    
''' Plotting of flux data to visualize before editing df ''' 

def flux_plot(df):
    
    df.plot(
        linestyle ='-', marker = '.', markersize = 5, linewidth = 1, 
        color = ['blue', 'darkorange']
        )
    
    plt.xlabel('Distance, x (cm)', labelpad=10)
    # $ signs allow for sub/supersctipt formatting 
    plt.ylabel('Flux in an Infinite Plane (n/cm$^2$s)', labelpad=10)
    plt.tick_params(axis="both",direction="in")
    
    # check how many columns are in the df
    dfnumcols = df.shape[1]
    
    Label = ['Heavy Water']
    if dfnumcols == 2:
        Label.append('Light Water')
        
    plt.legend(
        labels = Label, edgecolor='black', loc='upper right', fontsize=11
        )
    
    # Adds label text to plot, which is shown in the next function  
    plot_text(plt)
     
    plt.savefig('CombinedFlux.png', dpi=300)
    return plt

# This function adds plot text to the plot, which is sent to this function as an input
# variable
def plot_text(plt):
    # The plot is passed as an "object" into this function
    # We will add our desired text to a (x,y) location on the plot object
    
    # Axis specific properties of our plot can be changed
    ax = plt.gca()
    
    # Note the use of $^2# for superscript
    label = 'Max source, S (n/cm$^2$s)'
    
    # There are a few ways to add our data to the plot
    # Method 1: use ax.transdata, which allows us to set location using 
    # current plot data values (this is the default, so could omit transform
    # argument from plt.txt below) 
    
    # Method 1:
    x_loc = -82 # cm
    y_loc = 5.67e8 #n/cm^2 s
    trnsfrm=ax.transData
    
    # Method 2 for setting text location:
    # Distance can be given in 0 -> 1 location for each axis
    # 0 = origin of x or y plane and 1 = end of plane
    
    # Method 2:
    # x_loc = 0.33 # just past middle of x plane
    # y_loc = 0.96 # middle of y plane
    # trnsfrm = ax.transAxes
    
    # Some unicode arrow symbol codes:
    # down: u2193
    # right: u2192
    # left: u2190
    
    label = label + ' \u2192'
    
    plt.text(
        x_loc, y_loc, label,
        horizontalalignment='center', verticalalignment='top',
        fontsize='10', color='black', transform=trnsfrm
        )    
    
    return None

''' Reading file into Pandas dataframe and cleaning up data '''

def flux_input_raw():
    
    # This is the input file name of the doc you have dropped into your workspace.
    # The string input provided below must match exactly to the actual file name,
    # including any spaces, dashes, underscores, etc. Easiest is to copy/paste 
    # file name directly (e.g., similar to when you go rename a document,
    # and copy and paste the title) 
    Filename = 'Flux_InfPlane_CHE5834_D2O_R0.xlsx'
    
    InfinitePlaneFlux_df = pd.read_excel(Filename)
    
    # This must match the existing header in the spreadhseet, if there is one.
    # We could also ask Pandas to rename or just use column number notation
    DistanceLabel = 'Distance, x (cm)'
    FluxLabel = 'Flux (n/cm^2 s)'
    
    # x, y for unfiltered data plotting
    # x = InfinitePlaneFlux_df[DistanceLabel] 
    # y = InfinitePlaneFlux_df[FluxLabel]

    # Now we can clean up the data, which includes removing 0 and values that are
    # missing
    InfinitePlaneFlux_df.set_index(DistanceLabel, inplace=True)
    Condition = 0
    FluxID = InfinitePlaneFlux_df[FluxLabel]
    # Removes 0 values
    Filtered_InfPlnFlux_df = InfinitePlaneFlux_df[FluxID > Condition]
    # Drops missing values
    Filtered_InfPlnFlux_df = Filtered_InfPlnFlux_df.dropna(axis=0, how='any')
    
    # Renaming our read file to something shorter for ease
    df = Filtered_InfPlnFlux_df
    
    # More filtering using indexing of specific values
    Conditions = (df.index > -300) & (df.index < 200) & (df[FluxLabel] <9e6)
    df = df.drop(df[Conditions].index)
    
    # Checking what the flux data looks like
    # print (Filtered_InfPlnFlux_df.head(3))
    
    # We can also preview the plot, if desired     
    FluxCheckPlot = flux_plot(df)
    FluxCheckPlot.show()
    # FluxCheckPlot.savefig('FilteredInfPlnData.png', dpi=300)
    
    # This function returns the final, filtered dataframe
    return df

flux_input_raw()

def infplaneflux_calc():
    
    Distances = []
    LS_Flux_vals = []

    DistanceLabel = 'Distance, x (cm)'
    Fluxlabel = 'Calc Flux (n/cm^2 s)'
    
    # Chose arbitary x value range
    for dist in range (-400, 400, 1):            
        Distances.append(dist)
        InfPlnFlx = flux_inf_planr_source(dist)
        LS_Flux_vals.append(InfPlnFlx)
    
 
    InfPlFlux_df = pd.DataFrame(
        {
         DistanceLabel: Distances,   
         Fluxlabel: LS_Flux_vals  
            }
        )
    
    #plot = flux_plot(InfPlFlux_df)
    #plot.show()
    
    # plot.savefig('Flux_InfPlane_CHE5834_H2O.png', dpi=300)
    
    InfPlFlux_df.set_index(DistanceLabel, inplace=True)
    
    return InfPlFlux_df

# infplaneflux_calc()

''' Combining multiple data frames '''
  
def combined_flux_input_data():
    
    # Taking the two sets of flux calculations and plotting them together
    df_A = flux_input_raw()
    df_B = infplaneflux_calc()
    
    # Axis: 0 = index, 1 = columns, default 0
    AllFluxes = pd.concat([df_A, df_B], axis=1)
    
    Flux_df_= AllFluxes.loc[(AllFluxes.index <200) & (AllFluxes.index >=-200)]
  
    n_rows = 3
    # // operator divides number on its left by the number on its right
    # It rounds down the answer and returns a whole number
    rows_for_avg = np.arange(len(Flux_df_)) // n_rows
    # print (rows_for_avg)
    Flux_df_ = Flux_df_.groupby(rows_for_avg).mean()
    
    NewIndex = []
    for i in range (-200, 200, n_rows):
        newdist = i
        NewIndex.append(i)
    
    Flux_df_.index = NewIndex
    # print (Flux_df_)
    flux_plot(Flux_df_)
    plt.show()    
    return None

# combined_flux_input_data()
# flux_input_raw()