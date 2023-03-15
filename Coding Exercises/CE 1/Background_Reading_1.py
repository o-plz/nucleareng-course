
'''Background Reading - Coding Exercise 1
    These readings are used as a walk through for Python Basics that will
    help students complete future coding exercises and assignments.''' 

# 'Random' imports a built-in function that already exists in Python's download
import random

# Indentation is extremely important in Python! The following code shows why:
# This statement will work because there is no spacing before the code starts
print('indentation is important')

# This has a few random spaces before the code starts. Comment out the line
# below to clear the error!
    print('indentation is important')

# There are a few ways to print strings. This print statement will show the 
# difference between printing one string versus multiple strings.
print('I love nuclear engineering')
print('I', 'love', 'nuclear', 'engineering')


''' Variables '''

# Assigning a string to the variable called x
x = 'Nuclear Engineering is a cooler course than Nuclear Reactor Physics'
print(x)
# Printing the character x, which is not the string variable above, but
# it's own string
print('x')

# Prints the first letter in the string
print(x[0])
# Prints the last letter in the string
print(x[-1])
# Determines the length of the string
y = len(x)
print (y)
# Shows one way to print the entire string
print(x[0:67])
# Shows another way to print the entire string
print(x[0::])

''' Overloading Strings '''
# This section shows how to use different string variables inside
# math operators, and what they look like printed

x = 'checking how '
y = 'math operators work'

z = x + y
print(z)

z = x * 3
print (z)

''' Data Types '''
# Python has a few data types, like string (which we've seen here already),
# and float, which we will see here. Float is a numeric data type

# Assigning the string 2 to the variable y
y = '2'
print(y)
# Converts y from a string to a float
y = float(y)
print(y)

''' Lists '''
# Lists are very important and versatile in Python. Many of the assignments to
# come in this course use them

listofstrings = ['A', 'B', 'C']

# Determines length of list above (how many comma separated entries)
lengthlist = len(listofstrings)

# Prints the second element of the list (first item is at index 0, not 1)
print(listofstrings[1])

# Print the last element of the list
# Note: the length of the list is 3 --> there are 3 strings in the list, 
# BUT, asking the code for the string at index 3 would through an error
# this is because string A is at index location 0, B is at 1 and C is at 2
# for this reason, we ask for the string at location lengthlist - 1, which = 2
print(listofstrings[lengthlist-1])

# Bonus content: 
# list[-n] syntax gets the nth-to-last element,
# so list[-1] gets the last element, and list[-2] gets the second to last, etc.

# Print the last element of the list, regardless of length of list
print (listofstrings[-1])

# Print the first value in this list of integers below
listintegers = [1, 5, 9]
print(listintegers[0])

''' For Loops and Range '''

# For Loop examples:
for i in range(1, 5):
    # Starts counting at 1 because the start value is specified
    print (i)

# Line break that shows up as empty space in console (this comes in
# handy quite often in presenting print statements in a neat way)
print ('\n')     

for i in range(5):
    # By default, the loop starts counting from 0 because start not specified
    # Next, combining this loop with if statements
    if i <= 2:
        None
    else:
        print (i)

# Using a math operator within a For Loop
FavNumbers = [1, 5, 1988]
for i in FavNumbers:
    x = i * 4
    print (x)

''' Adding and Removing from List '''

# Create an empty list
new_list = []

# Loop over a range of numbers from default starting value of 0 to 
# number in brackets,here this would be 4
# Each value of i (0, 1, 2, 3, and 4) are added (not mathematically) to list
for i in range(5):
    new_list.append(i)

print (new_list)

# Next, we can remove items from a list
new_list.append('random string')
new_list.remove(2)

# This print statement allows us to see our next list, and shows
# what number was removed from the list (which was 2)
print (new_list, new_list.index(3))

# We can also see if a certain number is present in a list
if 3 in new_list:
    print('this item is in the list')

''' Iterating Over Multiple Lists '''

new_list2 = [1, 3, 5, 6]
new_list3 = ['cat', 'dog', 'goose']

# Zip is a feature that allows lists to be combined together,
# using a variable from one list then the other, back and forth
zipped_list = zip(new_list, new_list2)
print (zipped_list, '- this is the zipped list object')
print (list(zipped_list), '- this is the actual zipped list')

title_lists = ['list 1:', 'list 2:', 'list 3:']
all_lists = [new_list, new_list2, new_list3] 

# Looping through both lists above in order from 0th element to the last
# We don't have to use "i" and "j" notation below, but these are 
# pretty common to indicate the ith element of the first list and 
# jth element of the second list
# In this example, our second list, all_lists, is a list of lists,
# so each jth element is itself a list!
for i, j in zip(title_lists, all_lists):
    print ('\n') # little line break to chill out the code spacing
    print (i, j, len(j), 'printing next element of each list')
    
    # Adding in some list indexing stuff we learned above and
    # A quick little for loop:
    if i == title_lists[-1]:
        print (
            '\n', # bit more line breaking so we can read easier
            'Phew, making sense of lists is a lot of work.', '\n',
            'Give yourself a round of applause *claps in circle above head*',
            '\n'
            )

# Zipping 3 lists together
for x, y, z in zip(new_list, new_list2, new_list3):
    print (x, y, z)

''' The Random Function '''
    
# Random number from 0 to 10
print (random.randrange(10))
# Random number from 0 to 9, min and max of range both specified
print (random.randint(0,9))

