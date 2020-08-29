import random

MAX_NUMBER = 100
      
# prompt user for number of random numbers to generate
n = int(input("Enter number of random numbers to generate :"))

# TODO: Modify the code below so that the correct stats are printed out at the end

# loop to generate n random numbers and to print them all out
for i in range(n):
    random_number = random.randrange(0, MAX_NUMBER + 1)
    print("Random number " + str(i )+ " is " + str(random_number))

# print some stats
print()
print("Stats:")
print("Sum of all the random numbers is :")
print("Average of all random numbers is :")
print()
print("The largest number is  :")
print("Index of largest number is :")
print()
print("The smallest number is :")
print("Index of smallest number is :")
