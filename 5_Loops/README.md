# Loops

<!-- ## ```for``` Loops

### Q1

## ```while``` Loops -->

### Q1
Prompt the user for his/her gender. The user has to enter one of the following options: 'M' or 'F'. The program keeps prompting the user until the user enters a valid option.

A sample run of the code can be found below:

    What's your gender? Please enter M or F :T
    Wrong input!
    
    What's your gender? Please enter M or F :f
    Wrong input!
    
    What's your gender? Please enter M or F :F
    
    Thanks! Your gender is female.

### Q2
Write a program that prompts the user for two numbers. The program keeps prompting the user until  __both numbers are positive__ and __the sum of the two numbers is strictly smaller than 100__.

A sample run of the program can be found below:

```
Enter the first number: 90.5
Enter the second number: 0
Conditions not satisfied!

Enter the first number: 90.5
Enter the second number: 10.5
Conditions not satisfied!

Enter the first number: -5
Enter the second number: 50
Conditions not satisfied!

Enter the first number: 5.5
Enter the second number: 6.5

Thanks!
```

### Q3
Implement the function called calculate_average_length ( ) . The function takes in a
list of sentences and returns the average length of all the sentences in the given list.  

Example 1: If the function is invoked like this:
```
print(calculate_average_length(['apple','orange','Pear'])
```

the statement generates the following output:
```
5.0
```

Example 2: If the function is invoked like this: 
```
print(calculate_average_length([])
print(calculate_average_length(['','']) 
```

the statement generates the following output:
```
0.0
0.0
```

Test your code with q3-tester.py.

### Q4
Implement the function called `last_index_of()` that accepts a list of integers and returns the position of the last occurrence of the integer value (using positive indices).  
Note: You are not allowed to use list's `index` method .

```
>>> numbers = [3, 5, 9, 6, 0]
>>> numbers.index(5) 
1

>>> numbers.index(0) 
4

>>> numbers.index(10)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: 10 is not in list
```

<br>

Example 1:
If the function is invoked like this 
```
print(last_index_of([] , 3))
```

the statement generates the following output:
```
-1
```
  
>The function returns -1 because the value 3 is not found in the list.

<br>

Example 2: if the function is invoked like this: 
```
print(last_index_of([3, 5, 7] , 5))
```

the statement generates the following output:
```
1
```

>The function returns 1 because the value 5 is found at position 1.

<br>

Example 3: If the function is invoked like this:
```
print(last_index_of([3, 5, 7, 5, 4] , 5)) 
```

the statement generates the following output:
```
3
```

>The function returns 3 because the last occurrence of the value 5 is found at position 3.

### Q5
Iterating through a series of numbers ] Read q5.py and understand what the code is doing. Modify it minimally so that the correct stats are printed by the last six statements.

Sample run:
```
Enter number of random numbers to generate :10
Random number	0	is	96
Random number	1	is	6
Random number	2	is	61
Random number	3	is	31
Random number	4	is	50
Random number	5	is	95
Random number	6	is	48
Random number	7	is	42
Random number	8	is	97
Random number	9	is	17

Stats:			
Sum of all the random numbers is :543 
Average of all random numbers is :54.3

The largest number is :97 
Index of largest number is :8

The smallest number is :6 
Index of smallest number is :1
```

### Q6
Read q6.py and understand what the code is doing. Modify it minimally so that the correct stats are printed by the last six statements.

Sample run:
```
Enter number of Strings that you will enter :5
Enter string number 0:apple 
Enter string number 1:orangE 
Enter string number 2:BAnAna 
Enter string number 3:c
Enter string number 4:eeEE

Stats:
Longest string entered :orangE 
Index of longest string :1

Shortest string entered :c 
Index of shortest string :3

The string with the largest number of vowels :eeEE 
Index of string with largest number of vowels :4
```

### Q7
Iterating through a series of tuples. Read q7.py and understand what the code is doing. Modify it minimally so that the correct stats are printed by the last three statements.

Sample run:
```
Name :Shaun      , Age :38 , Sex	M
Name :Leslie     , Age :34 , Sex	M
Name :Dean       , Age :32 , Sex	M
Name :Sebastian  , Age :18 , Sex	M
Name :Gabriel    , Age :19 , Sex	M
Name :Xiao Wei   , Age :38 , Sex	F
Name :Cheryl     , Age :17 , Sex	F
Name :Sunita     , Age :14 , Sex	F
Name :Jolene     , Age :13 , Sex	F
Name :Jiwen      , Age :19 , Sex	F
Name :Amanda     , Age :38 , Sex	F

Stats:
Name of oldest male :Shaun 
Name of oldest female:Amanda 
Name of oldest Person:Amanda
```

### Q8
Write a program that prompts the user for numbers until he types 0 or a negative number. The program then prints out the average of all positive numbers entered.

A sample run is shown below:
```
Enter num :10 
Enter num :5 
Enter num :3 
Enter num :10 
Enter num :-1 

Average of positive integers entered: 7.0
```

### Q9 (Written Exercise)
This exercise requires you to trace through the code.

```
import random 
i = 0
sum = 0
while (i <= 10 and sum < 25):
    sum += random.randrange(0,11)
    print (sum)
    i += 1

print('The loop ran', i , 'times before it exit the loop with value', sum)
```

If the numbers generated by Line 05 are 6, 2, 0, 5, 10, 8, 1, 7 ,9, .. write down the output of the program.


### Q10
Write a program that prompts the user for a filename (assume valid filename). Then prints the sum of all the integers read from the file. A sample run is shown below:

```
Enter filename>q10-numbers.txt 
The sum is 37
```

You are given q10-numbers.txt with the following content:
```
10 
5
-2
```

### Q11
Write a program that prompts the user for a filename (assume valid filename). The file contains n integers per line.

```
10,20,30 5,9
-2
21,2,4
3,7,9,1,3
```

For each row in the data file, print the sum of the n integers to the console. A sample run is shown below (for q11-numbers.txt with content shown above):

```
Enter filename>q11-numbers.txt
60 
14
-2 
27 
23
```

### Q12
Write a program that prompts the user for two `str` values (for filenames) named `input_filename` and `output_filename`. It then reads the `input_filename` , and writes into `output_filename`. Each line in the output file will have a line number prefixed to the line content in input. For example, if the
following is the content of the input file:

```
A for apple
O for orange
P for pear
```

Output file should look like:
```
A for apple
O for orange
P for pear
```

>if the output file exists, overwrite the existing file. You could use the q12-data.txt as input file.

### Q13
Write a piece of code that does the following:

- The program first generates a random number between 1 and 100 (both inclusive). 
  <br />You can use the `randrange()` or `randint()` function from the `random` module to generate the number.
- The program then keeps prompting the user to guess the random number generated until the user's guess is correct. When the guess is wrong, the program gives a hint about whether the guess is too low or too high.

A sample run of the program can be found below. Note that in this sample run 95 is the random number generated in the beginning.

    Enter your guess (between 1 and 100) :34
    Your guess is too low!
    
    Enter your guess (between 1 and 100) :58
    Your guess is too low!
    
    Enter your guess (between 1 and 100) :73
    Your guess is too low!
    
    Enter your guess (between 1 and 100) :86
    Your guess is too low!
    
    Enter your guess (between 1 and 100) :99
    Your guess is too high!
    
    Enter your guess (between 1 and 100) :90
    Your guess is too low!
    
    Enter your guess (between 1 and 100) :95
    
    Bingo!

Another sample run is below. This time 47 is the random number generated in the beginning.

    Enter your guess (between 1 and 100):50
    Your guess is too high!
    
    Enter your guess (between 1 and 100):25
    Your guess is too low!
    
    Enter your guess (between 1 and 100):37
    Your guess is too low!
    
    Enter your guess (between 1 and 100):43
    Your guess is too low!
    
    Enter your guess (between 1 and 100):47
    
    Bingo!
    
__Note:__ You cannot reproduce the same output as shown above because your program will likely generate a different random number.

### Q14
#### Part I

Write a program that prompts the user for the items in his/her shopping cart. The program keeps prompting the user until there's no more item in the shopping cart. The program displays the total price of all the items in the shopping cart.

A sample run of the code can be found below:

    Do you have any item left in your shopping cart? Please enter Y or N :Y
    Please enter the name of the item : bread
    Please enter the price of the item : $2.2
    Please enter the quantity of the item : 2
    
    Do you have any item left in your shopping cart? Please enter Y or N :Y
    Please enter the name of the item : apples
    Please enter the price of the item : $0.5
    Please enter the quantity of the item : 6
    
    Do you have any item left in your shopping cart? Please enter Y or N :Y
    Please enter the name of the item : milk
    Please enter the price of the item : $5.3
    Please enter the quantity of the item : 1
    
    Do you have any item left in your shopping cart? Please enter Y or N :N
    
    Total price: $12.7

#### Part II

Now modify your code such that in the end the program prints out not only the total price but also all the items in the shopping cart.

A sample run of the program can be found below:

    Do you have any item left in your shopping cart? Please enter Y or N: Y
    Please enter the name of the item: bread
    Please enter the price of the item: $2.2
    Please enter the quantity of the item: 2
    
    Do you have any item left in your shopping cart? Please enter Y or N: Y
    Please enter the name of the item: apples
    Please enter the price of the item: $0.5
    Please enter the quantity of the item: 6
    
    Do you have any item left in your shopping cart? Please enter Y or N: Y
    Please enter the name of the item: milk
    Please enter the price of the item: $5.3
    Please enter the quantity of the item: 1
    
    Do you have any item left in your shopping cart? Please enter Y or N: N

    You've entered the following items:
        bread   $2.2	2
        apples  $0.5	6
        milk    $5.3	1

    Total price: $12.7


### Q15
Prompt the user for two strings. Keep prompting the user until the following conditions are satisfied:

1. Neither string contains a space.
2. The second string is longer than the first string.
3. Every character in the first string can be found in the second string.

A sample run of the program can be found below:

```
Enter the first string: SMU SIS
Enter the second string: SMUSIS
Conditions not satisfied!

Enter the first string: SMUSIS
Enter the second string: SMUSIS
Conditions not satisfied!

Enter the first string: SMUSIS
Enter the second string: SMUSMUSMU
Conditions not satisfied!

Enter the first string: SMUSIS
Enter the second string: SMUSISS

Bingo!
```

### Q16
Write a program called q16.py. The program will prompt the user for two numbers. Call them `n1` and `n2`. Keep prompting the user until the sum of `n1` and `n2` is divisible by 3. Then display all numbers between `n1` (inclusive) and `n2` (inclusive) in increasing order. Note that `n1` may be smaller than `n2`, equal to `n2`, or greater than `n2`. You need to handle all scenarios. You are free to choose any loop construct together with any `if/else` construct for this question.

Sample Runs:
```
D:\5_Loops\while_loops>python q16.py
Enter nl>3 
Enter n2>4 
Invalid!

Enter nl>3 
Enter n2>6 
3 4 5 6

D:\5_Loops\while_loops>python q16.py
Enter nl>6 
Enter n2>3 
3 4 5 6
```

**Note:**
- The sum of 3 + 4 is 7 which is not divisible by 3.
- The sum of 3 + 6 is 9 which is divisible by 3. Thus, all the numbers between 3 (inclusive) and 6(inclusive) are printed.


### Q17
Implement the function called generate_initials0. It takes in a list of names, and returns a list of tuples in the format of (initial, name).  

To generate the initials, do the following:
1. take the first character of each word in the name.
2. If the name consists of 1 word, take the first 2 characters of the word.
3. If the name consists of more than 3 words, take only the first character of the first 3 words.
4. [Challenging] If the initial has already been used, then append a running number behind it (2,3, ..) for the 2nd,3rd,.. occurrences.

Example 1: If the function is invoked like this:
```
name list = ['Alan TAN Jun Jie', 'Apple LIM', 'Ann Lee'] 
print(generate_initials(name_list))
```

the statement generates the following output:
```
[('ATJ', 'Alan TAN Jun Jie'), ('AL', 'Apple LIM'), ('AL2', 'Ann Lee')]
```

Test your code with q17tester.py.

### Q18
A palindromic number is a number that is the same when written forwards or backwards.  
The first few palindromic numbers are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, ...   
A lot of positive integers of 2 digits or more can produce a palindromic number by repeatedly reversing the digits and adding the new number to the original number.

For example, given the number 5280  
Iteration 1:    5280    +   0825    =   6105  
Iteration 2:    6105    +   5016    =   11121  
Iteration 3:    11121   +   12111   =   23232 (this number is palindromic)  

When `produce_palindromic_num` function is invoked with number, it returns the first palindromic number generated.  
Implement the `produce_palindromic_num` function. 

You can assume number is
- a positive integer of 2 digits or more and
- the number will definitely generate a palindromic number

Eg. 1: If the function is invoked like this:
```
print(produce_palindromic_num(5280))
```

the statement generates the following output:
```
23232
```

Eg. 2: If the function is invoked like this:
```
print(produce_palindromic_num(89)) 
```

the statement generates the following output:
```
8813200023188
```

### Q19
Implement a one-player Mastermind game (player versus computer). You can find the rules of the game here: https://www.wikihow.com/Play-Mastermind

The game involves 6 colors (R: Red, Y: Yellow, B: Blue, 0: Orange, G: Green, V: Violet).
1. The computer program you write will generate the secret code (of colors) and provide feedback for each guess. The secret code should be randomly generated for each new game. Use the random package to get a number between 0 and 6 (exclusive). Then you'll need to convert that into a color (e.g., 'red') using an if-else clause. The secret code can consist of repetitions of the same color. For example, "GYYG".
2. The player enters the guess. The entry 'RYBO' would be say, a guess of Red, Yellow, Blue, Orange.
3. Print out the number of correct matches (right color at right position) and the number of partial matches (right color but wrong position).

For example, if code is 'RRBB', and the guess is 'BBRB', then it should display 1 correct match, 2 partial matches.

4. Your program should prompt the user repeatedly until the correct guess is inputted.
5. When the correct guess (all exact matches) is input, the system prints out a congratulation message and informs the user his number of attempts at guessing.

A sample run is shown below:
```
Enter guess:BBOO
1 exact matches, 0 partial matches

Enter guess:ASMU 
Invalid colors(ASMU)!

Enter guess:BOVG
1 exact matches, 1 partial matches

Enter guess:YBYV
2 exact matches, 2 partial matches

Enter guess:BYVY
2 exact matches, 2 partial matches

Enter guess:YBVY
You guessed the key: YBVY It took you 6 guesses
```

You are given q19.py. Complete the required functions specified in the q12.py and use them to solve this problem.

### Q20
Write a program that prompts the user for his/her name. A name can consist of only alphabets and space. If the name entered by the user does not satisfy the condition, you should prompt the user for name again.

Sample run of the program is shown below:
```
Enter name :John Smith! 
Invalid name

Enter name :JohnSmithl 
Invalid name

Enter name :John Smith 
Hello John Smith!
```

### Q21
Write a program that simulates Random Number Guessing Game.

The program should pick a random number between 1 and 100 (both inclusive) and prompt the user to guess number until he guesses correctly. If the user's guess is higher than the random number generated, the program should display "High! Try again. If the user's guess is lower than the random number generated, the program should display "Low! Try again.

If the user guesses correctly, display the count of number of guesses the user took to get it correct and re-start the game if the user wishes to do so by entering Y at the prompt "Do you want to play again?"

Sample Run 1:
```
Enter your guess(1 to 100) :9p
Wrong input.

Enter your guess(1 to 100) :26
Low! Try again

Enter your guess(1 to 100) :46
Low! Try again

Enter your guess(1 to 100) :65
High! Try again

Enter your guess(1 to 100) :59
Low! Try again

Enter your guess(1 to 100) :61
Congrats!

You guessed in 6 attempts

Do you want to play again(Y for yes)? N 
Bye!
```

Sample Run2:
```
Enter your guess(1 to 100) :26
Low! Try again

Enter your guess(1 to 100) :56
High! Try again

Enter your guess(1 to 100) :35
Congrats!

You guessed in 3 attempts

Do you want to play again? Y

Enter your guess(1 to 100) :55

# rest of code not shown for brevity
```

### Q22
Counting in binary is similar to counting in any other number system. Beginning with a single digit, counting proceeds through each symbol, in increasing order. Decimal (or base-10) counting uses the symbols 0 through 9, while binary only uses the symbols 0 and 1. Read more about how a decimal number can be converted to its binary equivalent:
- http://www.is.wayne.edu/olmt/binary/page3.htm 
- http://www.wikihow.com/Convert-from-Decimal-to-Binary

Let us see the method to convert decimal number 32(base 10) to its binary equivalent.
>32 divided by 2 gives 16 and remainder 0   
>16 divided by 2 gives 8 and remainder 0  
>8 divided by 2 gives 4 and remainder 0   
>4 divided by 2 gives 2 and remainder 0  
>2 divided by 2 gives 1 and remainder 0  
>1 divided by 2 gives 0 and remainder 1  

Do you notice that you are dividing the given decimal number by 2 and subsequently in every iteration, the quotient is divided by 2? The binary number is the sequence of remainders in reverse, from the bottom remainder to the top remainder.

Write a program that converts a positive integer number to its binary equivalent following the procedure explained above. You can check if your conversion is correct using the built-in function.

Try the built-in function bin in python that converts decimal number to its binary equivalent

```
>>> bin(10) 
'Ob1010'

>>> bin (32)
'Ob100000'       # Ob indicates that it is binary representation.
```

Sample Run:
```
The decimal number is 32
Binary equivalent of 32 is 100000
```

### Q23
Your primary school going neighbor wants you to create a program for him to practice multiplication tables 2 to 10. Design a multiplication quiz user interface as shown below:

```
Menu:
    1.	Choose a table to practice
    2.	Practice with a random table
    3.	Quit
Your choice? 1
The multiplication table you wish to practice?5
1 X 5 = 5 Correct!
2 X 5 = 5 Wrong!
3 X 5 = 15
Correct!
4 X 5 = 15
Wrong!
5 X 5 = 25
Correct!
6 X 5 = 30
Correct!
7 X 5 = 35
Correct!
8 X 5 = 40
Correct!
9 X 5 = 45
Correct!
10 X 5 = 50
Correct!
Your score: 8/10

Menu:
    1.	Choose a table to practice
    2.	Practice with a random table
    3.	Quit
Your choice? 2
You will be quizzed on multiplication table: 3
1 X 3 = 3 Correct!
2 X 3 = 5 Wrong!
3 X 3 = 9 Correct!
4 X 3 = 12 Correct!
5 x 3 = 15 Correct!
6 X 3 = 18 Correct!
7 X 3 = 21 Correct!
8 X 3 = 24 Correct!
9 X 3 = 27 Correct!
10 X 3 = 30 Correct!
Your score: 9 / 10

Menu:
    1.	Choose a table to practice
    2.	Practice with a random table
    3.	Quit 
Your choice? 3
Bye!
```

**Note:**
- For menu options 1 and 2, the program is supposed to quiz the user for the specific multiplication table from n * 1 to n * 10 where n is the multiplication table number chosen by the user in option 1 and for option 2, n is randomly generated by the program.
Menu option 3 ends the quiz.
- Design the program in such a way that there is no repetitive code. If you think carefully, options 1 and 2 do the same asking quiz questions 10 times and printing the score. Hence, perhaps you could define a function that takes in a parameter for the chosen quiz table.

Solve the problem by writing functions and calling them as per the flow required. Every function should be modular in nature i.e. each function should be designed to do one specific task. For example, there could be a function that displays the menu, there could be another function to print the quiz and display the
score, etc