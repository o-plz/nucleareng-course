'''Coding Exercise 1 - Solutions'''

import random

# List of past tense verbs, with as many entries as you like
verb_past = [
    'barfed', 'walked', 'ate', 'skipped', 'drove', 'frolicked', 
    'laughed', 'screamed', 'galloped', 'warmed'
    ]

# List of plural nouns
noun_plural = [
    'dogs', 'chairs', 'croissants', 'giraffes', 'toasters', 'pants', 'hippos'
    ]

# List of adjectives
adjective = [
    'great', 'moist', 'sassy', 'easy', 'silly', 'smelly', 'rad', 'tasty'
    ]

# List of singular nouns
noun_singular = [
    'photograph', 'pizza', 'dress', 'car', 'cat', 'crystal ball', 'cake'
    ]

# The "story" list was included in the excerise PDF, it just needed to be
# copied over into Python
intro = ' Ben and I were studying in the Head Rest for our Nuclear Engineering midterm. \n'
allblurbs = [
    'We', 'for the first hour, reviewing the unit on', 
'Ben commented that the Nuclear Engineering course was extremely', 
'. This was mainly because all semester he only watched TV shows on', 
'and talked to his', '. I thought this was very', ', so I went home and'
] 

# Another option students could take was using the /n command to
# clean up the code. Either option is okay
allblurbs = [
    'We', 'for the first hour, reviewing the unit on', 
    '\n Ben commented that the Nuclear Engineering course was extremely', 
    '.\n This was mainly because all semester he only watched TV shows on', 
    'and talked to his', '.\n I thought this was very', ', so I went home and'] 

# Some various print statements to check that things are working
# print (allblurbs)
# testing the length of the pre-written text blurb list
# print(len(allblurbs))

# Next, the words from the previous list are randomly selected
# to be placed into the story
# blurb1 = 'We'
mLib1 = verb_past[random.randint(0, len(verb_past) - 1)]
# blurb2 = 'for the first hour, reviewing the unit on'
mLib2 = noun_plural[random.randint(0, len(noun_plural) - 1)]
# blurb3 = '\n Ben commented that the Nuclear Engineering course was extremely'
mLib3 = adjective[random.randint(0, len(adjective) - 1)]
# blurb4 = '.\nThis was mainly because all semester he only watched TV shows on'
mLib4 = noun_plural[random.randint(0, len(noun_plural) - 1)]
# blurb5 = 'and talked to his'
mLib5 = noun_singular[random.randint(0, len(noun_singular) - 1)]
# blurb6 = '\n I thought this was very'
# blurb7 = ', so I went home and'
mLib6 = verb_past[random.randint(0, len(noun_singular) - 1)]

# Putting it all together in a list, then appending it to the intro list
# from earlier
alllibs = [mLib1, mLib2, mLib3, mLib4, mLib5, mLib3, mLib6]

fulllib = []
fulllib.append(intro)

# Loop to add ith and jth elements of each of the two lists, alternating
for i, j in zip(allblurbs, alllibs):
    fulllib.append(i)
    fulllib.append(j)
    
# Joining each of the elements together
fulllib = (' '.join(fulllib))

print (fulllib)