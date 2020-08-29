# list of person tuples 
# (name, age, gender)
persons = [("Shaun", 38, 'M'),
        ("Leslie", 34, 'M'),
        ("Dean", 32, 'M'),
        ("Sebastian", 18, 'M'),
        ("Gabriel", 19, 'M'),
        ("Xiao Wei", 38, 'F'),
        ("Cheryl", 17, 'F'),
        ("Sunita", 14, 'F'),
        ("Jolene", 13, 'F'),
        ("Jiwen", 19, 'F'),
        ("Amanda", 38, 'F')]


# TODO: Modify the code below so that the correct stats are printed out at the end
    
# loop to retrieve every single Person from pFac and print out information regarding each Person
for i in range(len(persons)):
    print (persons[i])
   
# print some stats
print()
print("Stats:")
# for all cases below, if there is a tie for ages, print the one with the larger index
# if there is a tie between oldest male an oldest female, print the one with the larger index
print("Name of oldest male  :")
print("Name of oldest female:")
print("Name of oldest Person:")

import datetime
now = datetime.datetime.now()
print (now.timetuple())
print (now.year)