
# prompt user for number of random numbers to generate
n = int(input("Enter number of Strings that you will enter :"))


# TODO: Modify the code below so that the correct stats are printed out at the end
# loop to allow user to enter n Strings
for  i in range(1, n + 1):
    value = print("Enter string number " + i + ":")


# print some stats
print()
print("Stats:")

# for all cases below, if there is a tie, the EARLIER string should be printed.
print("Longest string entered  :") 
print("Index of longest string :") 

print("\nShortest string entered  :") 
print("Index of shortest string :") 

# vowels are the characters AEIOUaeiou.
print("The string with the largest number of vowels :") 
print("Index of string with largest number of vowels :") 
