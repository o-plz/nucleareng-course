'''Background Reading - Coding Exercise 2
    This background reading covers information that some students
    may be familiar with if they completed option 2 of assignment 1.'''

# Import statements for packages needed is done at the beginning of
# the code
import periodictable as pdt
import random as rd

# This imports a specific function from package
from periodictable import hydrogen


'''Using If/Else Statements'''

elementslist = ['uranium', 'plutonium', 'mercury']

# The elements at each index are 0=uranium, 1=plutonium, and 2=mercury
# If we want to access one of these elements, we have to use an index
# of 0, 1, or 2. Other index values will give an error, which can be
# seen if the following line in uncommented: 
# print (elementslist[3])

# The above gives the error "IndexError: list index out of range",
# which is expected
# We can get around this with some if-else statements

# Let's define the max possible value of the list index (the length - 1)
# Python starts numbering at 0, so while the length of elementslist is 3, 
# elementslist[3] doesn't exist
max_user_value = len(elementslist) - 1

# To demonstrate this example, we are going to create a fake user input
desired_list_element = rd.randint(0, 10)
print ('You chose list index number: ', desired_list_element)

if desired_list_element > max_user_value:
    # A possible solution could be picking a random number in the 
    # correct range and reassigning desired_list_element to this new value
    desired_list_element = rd.randint(0, max_user_value)
    
    # A line break, \, is added when the code is too long (generally > column 80)
    print ('Your chosen value was too high, a value of', desired_list_element,\
           'was chosen.')
    # Another way to "wrap" the text on the screen (so it doesn't run on
    # horizontally), is to put round brackets around portions of your code.
    # The practice is to hit enter immediately after the start of the brackets,
    # then once again before the closing bracket, visually separating the 
    # bracketed text with a bracket above and a bracket below, as follows:
    print (
        'This is the element at the chosen index #: ', 
        elementslist[desired_list_element]
        )
    
    # The above method doesn't require using the \ line break. Either is okay
    # to use, depending on style preference

# If the value randomly chose is less than the max value, an elif statement
# is used to show that the value chosen was okay    
elif desired_list_element <= max_user_value:
    print ('Your value is within the list index.')
    print (elementslist[desired_list_element])

# The following code defines two input values, A and B, and uses if/elseif 
# statements it determine if the values are within a specified range
# It specifies that if A is a certain value (5), B must be less than 35
A = 5
B = 33
if A == 5:
    print ('double equals sign used to check if A is equal to 5')
    if B > 35:
        print (B, ': I do not like this value of B')
    elif B < 35:
        print (B, ': This value of B is okay')
else:
    None

# The following line break that shows up in console
print ('\n')

''' Defining Functions'''

# Function that returns the y value of a line of slope 4
def line_solver(x, y_int):
    m = 4
    y = m * x + y_int
    return y

# To use the function, it must be called using its name, and inputting
# the values it needs to run. This can be seen below:
print ('the value of y is:', line_solver(2, 4))
print ('with explicit definition of variables, the value of y is still:', \
       line_solver(y_int=4, x=2))

# Next, we can define the same function, but it returns 2 variables, 
# y and m
def line_solver_2(x, y_int):
    m = 4
    y = m * x + y_int
    return y, m

# We can assign these returned variables to variables within the code
# This allows the variables to be used elsewhere
y_val, slope = line_solver_2(x=2, y_int=4)
y_val = line_solver_2(x=2, y_int=4)[0]

# Defining x, y, and z outside of a function to show how Python defines
# variables inside and outside functions
x = 4
y = [1, 3, 4]
z = []

constant = 4

def testfunction(input1):
    # Below is the function docstring
    '''
    Calculates the values of x and y.
    
    Args: 
    input1: list input
    
    Return: returns two objects, x and y.
    x is an integer or float
    y is a list 
    
    Side effects:
    the first element of the input list is modified after y is calculated 
    the list z is appended to using on a for-loop with a range 
    dictated by the second element of the list, y
    '''
    
    x = 10 * constant
    # This variable y is not the same as y outside the function
    # The scope and memory inside the function does not carry over 
    # unless a "mutable" variable is being changed, e.g., a list
    y = [i * 2 for i in input1]
    
    # This changes the first entry of a list input
    # which carries over to the memory outside the function as lists
    # are mutable or changeable data types
    input1[0] = 10
    for i in range(y[2]):
        q = i + 1
        z.append(q)
    z[0] = 10
    return x, y

# Calling the function does not update previously defined x and y (outside function) 
# Even though there are variables with same names inside testfunction, 
# their scope is only inside that function
testfunction(y)
print ('\n')

print (y)
print (z)

print ('x and y are equal to:', x, y, ': x is not updated.')
print ('the first element of the list y was updated')

# If x and y are redefined outside of the function, in the scope of the module, 
# they are updated (here, based on function output) 
x, y = testfunction(y) 

print ('\n')
print ('x is equal to:', x, y, ''': x and y are now equal to the function 
returns that they were reassigned to.''')

print ('''z was a list defined outside of the function and was added to 
inside the function. z was updated twice because the function was called twice: 
''', z)

print ('\n') 


''' Periodictable Package Examples'''

''' This next section has been commented out since there are many print 
statements. Feel free to uncomment (highlight then Ctrl + /) as needed. '''

''' Note: if commenting + uncommenting large blocks of code results in a weird 
indentation, (where code is no longer flush with the left-hand-side margin, using 
shift + tab keyboard commands on the highlighted lines of code can resolve this 
for a large block (instead of manually backspacing indentation of each line). '''

# If we only want to access particular elements by name:
print (hydrogen.mass)

# We could also access particular elements as symbols
print (pdt.Li.mass, pdt.H.mass, pdt.Ca.mass)

# Accessing mass_units attribute
print (pdt.H.mass_units)

# Assigning this element to our own variable
hydr = pdt.H
print (hydr.mass_units)

# Assigning mass of element to our own variable
mass_hydr = hydr.mass
print (mass_hydr)

# Assigning our own variable (H_3) to the tritium isotope of hydrogen
H_3 = pdt.H[3]
print (H_3.number, 'this is the number of protons or atomic #, Z')
print (H_3.isotope, 'this is the atomic mass number (A = Z + N)')