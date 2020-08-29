# Decision Logic

#### Q1

Write a program that prompts the user for his/her name and gender. The program must greet the user politely (Mr or Miss).  
If the user does not enter his/her gender correctly, leave out the salutation (Mr/Miss).

```
Enter name: Lance
Enter gender (M or F) :M 
Welcome, Mr Lance!
```
```
Enter name: Xiu Ling
Enter gender (M or F):F 
Welcome, Miss Xiu Ling
```
```
Enter name: Wei Xiang
Enter gender (M or F):
Welcome, Wei Xiang!
```

#### Q2
Write a program that prompts the user for a month number and prints out the number of days in that month. 
If the user enters an invalid number (e.g. **-5, 0 or 13**), show an error message.  
There are 31 days in the following months: 1, 3, 5, 7, 8, 10 and 12. There are 30 days in the remaining months except February.
For simplicity, you may assume that there are always 28 days in February and the user always enters an integer.  
```
Enter month as a number:14  
Enter a number between 1 and 12 only.
```
```
Enter month as a number:8
There are 31 days in this month.
```
```
Enter month as a number:4
There are 30 days in this month.
```

#### Q3
Write a program that prompt the user for a number, n. Continue prompting the user for n strings, 
and print out the shortest and longest string followed by the length in parentheses behind.  

If there are more than 1 string that has the same shortest or longest length, only the later string is considered.

```
Enter n: 5
Enter string 1: apple
Enter string 2: pear 
Enter string 3: cherry 
Enter string 4: pineapple
Enter string 5: grape
The shortest string is pear (4)
The longest string is pineapple (9)
```

```
Enter n: 5
Enter string 1: apple
Enter string 2: durian 
Enter string 3: cherry 
Enter string 4: pineapple
Enter string 5: grape
The shortest string is grape (5)
The longest string is pineapple (9)
```

#### Q4
Write a function called is_ good_	sword. It must return True if the following
conditions are met:  
- The password must be at least 6 characters long and at most 20 characters  
- It must contain at least one lowercase letter, one uppercase letter, and one number. Otherwise, the function must return `False`.  

Note: You are supposed to think of test cases (similar to the ones in 01 - Q5.  
An example is shown below:  

```
result = isgoodpassword(") 
print('Expected: False')
print('Actual:' + str(result))
```

#### Q5
Write a function called `count_characters` that takes in 2 parameter, a string `input_string` and a single character string `char`.  
The function is supposed to return the number of `char` appearing in the input parameter `input_string` or None if there isnt any of 
the character that appears in `input_string`. The `char` is **case-sensitive**.

_You are **NOT** allowed to use `count` method in this exercise_

```
>>> print ("Number of 'l' in 'hello' : ", count_characters ("hello", 'l' ) )
Number of 'l' in 'hello': 2
```
```
>>> print ("Number of 'e' in 'HELLO' : ", count_characters ("HELLO", 'e' ) )
Number of 'e' in 'HELLO': None
```
```
print ("Number of 'e' in 'hello there' : ", count_characters ("hello there", 'e' ) )
Number of 'e' in 'hello there': 3
```

#### Q6
Implement the `calculate_ticket_price` function. The function takes in 1 parameter: `age (type: int)`  
You can use the following table for reference

Age Range         | Ticket Price
------------------|-------------
Children (below 4yo)    | Free ($0)
Children (4 - 12)       | $56
Adult (13 - 59)         | $76
Senior (60yo and above) | $38

The following are some sample output when the function is invoked
```
>>> print ( calculate_ticket_price(13) )
76
```
```
>>> print ( calculate_ticket_price(12) )
56
```
```
>>> print ( calculate_ticket_price(99) )
38
```
```
>>> print ( calculate_ticket_price(3) )
0
```