# File Reading

## Q1: Reading Files

### Part (a) 

Define a function called `print_alternate_lines` that takes in the name of a file as its parameter. The function prints out alternate lines from the file, starting from the first line. That is, the function prints out the first line, the third line, the fifth line, etc. of the file until the file ends.

For example, if the file looks like the following:

```
1
22
333
4444
4444
333
22
1
```

The function should print out the following output:

```
1
333
4444
22
```
```
# Test Cases:

print("Test Case #1:")
print()
print("Expected:")
print("1\n333\n4444\n22\n")
print("Actual  :")
print_alternate_lines('q1-input-1.txt')

print("\n==========\n")

print("Test Case #2:")
print()
print("Expected:")
print("Line 1\nLine 3\nLine 5\n")
print("Actual  :")
print_alternate_lines('q1-input-2.txt')
```

### Part (b)

Define a function called ```print_alternate_columns``` that takes in the name of a file as its parameter. Each line of the file contains several columns, separated by the symbol ```'&'```. The function prints out alternate columns of the file, starting from the first column. That is, the function prints out the first column, the third column, the fifth column, etc., still separated by ```'&'```.

__You can assume that each line contains at least one column.__ However, different lines may have different numbers of columns.

For example, if the file looks like the following:

```
apple & orange & pear
banana & cherry & durian & mango & starfruit
watermelon & peach
```

The function should print out the following output:

```
apple & pear
banana & durian & starfruit
watermelon
```
```
# Test Cases:

print("Test Case #1:")
print()
print("Expected:")
print("apple & pear\nbanana & durian & starfruit\nwatermelon\n")
print("Actual  :")
print_alternate_columns('q1-input-3.txt')

print("\n==========\n")

print("Test Case #2:")
print()
print("Expected:")
print("col1&col3&col5\ncol1&col3\n1 & 3 & 5 & 7\na&c&e\n")
print("Actual  :")
print_alternate_columns('q1-input-4.txt')
```
## Q2: Universities

You are given a file that contains exactly 4 columns in each row, separated by tabs. The 4 columns represent the following information:

```
name_of_a_university    acronym    year_founded    number_of_undergraduate_students
```

For example, the file may look like the following:

```
National University of Singapore    NUS    1905    27972
Nanyang Technological University    NTU    1981    24300
Singapore Management University    SMU    2000    7827
University of California, Berkeley    Berkeley    1868    29310
Harvard University    Harvard    1636    6700
University of California, Los Angeles    UCLA    1919    30873
```

### Part (a)

Define a function called ```get_universities_founded_before()```. This function takes in the name of a file as described above and an integer called ```year``` as its parameters. The function returns a list of strings that represent the names of the universities in the given file which were founded __before__ the specified ```year```.

For example, if the file is as shown above and ```year``` is ```1905```, then the function should return ```['University of California, Berkeley', 'Harvard University']```.

```
# Test Cases:

my_list = get_universities_founded_before('universities-1.txt', 1905)
print("Test Case #1:")
print("Expected:", end='')
print("['University of California, Berkeley', 'Harvard University']")
print("Actual  :", end='')
print(my_list)

print("\n==========\n")

my_list = get_universities_founded_before('universities-2.txt', 1800)
print("Test Case #2:")
print("Expected:", end='')
print("['University of Cambridge', 'University of Oxford']")
print("Actual  :", end='')
print(my_list)
```

### Part (b) 

Define a function called ```get_average_num_students()```. This function takes in the name of a file as described above and returns the average number of undergraduate students of all the universities in the given file. If the file is empty, the function returns 0.0.

```
# Test Case:

print("Expected: 21163.666666666668")
print("Actual  : " + str(get_average_num_students('universities-1.txt')))

### Part (c) 

Define a function called ```search_with_keyword()```. This function takes in the name of a file as described above and a string that represents a keyword. The function returns a list of strings that represent the __acronyms__ of the universities whose __full names__ contain the given keyword.

For example, given the file as shown above, if the keyword is ```'California'```, then the function should return ```['Berkeley', 'UCLA']```.

Your search needs to be __case-insensitive__. So searching for ```'california'``` or ```'California'``` should give you the same results.
```
```
# Test Cases

print("Expected: ['Berkeley', 'UCLA']")
print("Actual  : " + str(search_with_keyword('universities-1.txt', 'california')))
```
## Q3: Temperatures 

You are given a file called `'temperatures.txt'` that stores some patients' temperature readings. Each line of the file is about a single patient. The patient's name is displayed first followed by a sequence of temperature values. The name and the different temperature values are separated by tabs. Note that the numbers of temperature readings are different for different patients.

Read in this file and print out the minimum and maximum temperature readings of each patient.

__You can assume that for each patient, there is at least one temperature reading in the file.__

Your program should display the following output:

```
Kate: 36.3, 37.6
Larry: 36.1, 38.4
Jerry: 37.6, 38.9
```

## Q4: Transactions

You are given a file called `"transactions.txt"` that contains the transaction history of a person's credit card. Each line of the file contains the following three columns: (1) A date in dd-mm-yyyy format. (2) A text description of the transaction. (3) The amount of the transaction. The three columns are separated by tabs.

Note that these transactions are not sorted in any particular order. 

### Part (a) 

Write a piece of code that reads this file and writes to an output file called `"transactions-output-1.txt"`. The output file should contain those transactions where the transacted amount is $30.00 or above.

Your generated file should contain the following lines:

```
09-12-2016    NTUC FairPrice  $59.43
08-01-2017    Shell Station   $47.56
09-03-2017    SingTel $31.50
08-01-2017    SingTel $32.10
21-12-2016    SIA     $546.90
19-03-2017    NTUC FairPrice  $108.32
```
### Part (b) 

Write a piece of code that reads this file and writes to an output file called `"transactions-output-2.txt"`. The output file should group the transactions by months, with the total amount per month shown. The order of the months doesn't matter.

The output file looks like the following:

```
03-2016: total transaction amount is $21.3
    Popular	$21.30

12-2016: total transaction amount is $606.3299999999999
    NTUC FairPrice	$59.43
    SIA	$546.90

01-2017: total transaction amount is $79.66
    Shell Station	$47.56
    SingTel	$32.10

03-2017: total transaction amount is $139.82
    SingTel	$31.50
    NTUC FairPrice	$108.32

02-2017: total transaction amount is $49.7
    Popular	$25.40
    Shaw Theatres	$24.30
```

## Q5

You are given a file called `q5-phone-book.txt`. The format is as follows:
```
<name>|<Mobile|Home|Pager|Fax>|<Phone Number>
```
A sample is shown below:
```
George Leung|Mobile|98987676 
Eric Wong|Home|67449908
Michelle Lee|Mobile|96667777 
Eric Wong|Mobile|91234567 
Michelle Lee|Pager|88776655 
Michelle Lee|Fax|88776656
```
(a) `get_phone_book()`:The function takes in a filename and returns a dictionary where the key is the name-<Mobile|Home|Pager|Fax>, and the value is the phone number.
(b) `get_phone_numbers_for()`:The function takes in a `str (name)` and a dictionary with key containing <name›-Mobile|Home|Pager|fax and value that contains contact number. The function must return a dictionary that represents contact numbers of the name where the key is a `str` value (Mobile or Home or Pager or Fax) and the value is the phone number.
You can test your code with `q5-tester.py` provided.


### Q6
Write a program to read from the given file called words.txt. Every line in words.txt contains one single word. The program is supposed to read words in the file and print all words along with the count of distinct vowels present in the word as shown in the sample run. You may want to write additional functions in the file, one function perhaps to count the number of distinct vowels in every word etc.

Sample run (with the given words.txt file):

```
python 1 
dynamic-typed 3 
function 3 
parameter 2 
argument 3
str 0
int 1
float 2

... rest not shown for brevity
```

### Q7
You are given a file called q3-tester.py. Define the following functions in q7.py:

- `get_english_dictionary()`: The function takes in a filename and returns the list of words from the specified file. The file will contain one word per line. Do remember to remove the trailing end of line character.
- `check_spelling()`: The function takes in a sentence and returns a list of words from the text that are possibly misspelled, i.e., a list of words that are not found in the English dictionary. 

For example, `check_spelling("I sturddy at Singapore Managment Univercity")` should return `["sturddy", "Managment", "Univercity"]`.

(words_alpha.txt is taken from https://github.comidwvlienglish-words. Note how the functions in q7.py are used in q7-tester.py)

### Q8
Write a python file called q8.py that reads a file and prints all the lines that contain a specific word (passed to the Python script).

**Hint:**  
When values are passed to the Python script during execution, the arguments are stored in this variable called `sys.argv`. As an example of how to use `sys.argv` variable, observe the code in sample.py script below:

```
import sys

if len(sys.argv) == 3: 
    print("first:", sys.argv[3]) 
    print("second:", sys.argv[1]) 
    print("third:", sys.argv[2])
```

A sample run of the sample.py is shown below:
```
c:\is111>python sample.py apple orange
first: c:\is111\sample.py
second: apple 
third: orange
```

We have given you seashells.txt in the resources. You can pass the filename and word to be searched for on the command line as shown below: 

(Observe the first line in the sample shown below. The filename we would want to read is "seashells.txt" and the word we are looking for is "sure")

```
c:\islll>python q8.py sure seashells.txt 
The shells she sells are surely seashells. 
I'm sure she sells seashore shells.

c:\is111>python q8.py python seashells.txt 
No line found.
```

Q8 is trying to implement code for a command available in Unix, called grep, The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

### Q9
Write a program q6.py that reads from q6-basic.txt, multiplies corresponding elements in 2 lists, and writes those products to output.txt whose value is larger or equal to the <check value>.  
The input file format is as follows:  
Format is as follows: 

A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub>@B<sub>1</sub>, B<sub>2</sub>, ...,B<sub>n</sub>#<check value>  

Below is an example:

```
1,2,3@3,4,5#8
1,2@3,4,5#4
1,2,3@4,5#10
```

Program q9 does the following:
1. read q9-basic.txt
2. multiply A<sub>1</sub> with B<sub>1</sub>, A<sub>2</sub> with B<sub>2</sub> ..., A<sub>n</sub> with B<sub>n</sub>
3. It checks the result of each multiplication. For results whose value is greater than or equal to the <check value>, writes the multiplication value to the output file.

For example:
- The result of the first line is 1 x 3 = 3, 2 x 4 = 8, and 3 x 5 = 15. Only the numbers 8 and 15 will be written to output.txt (as the check value is 8).
- The result of the second line is 1 x 3 = 3, 2 x 4 = 8, 5 = 5. Only 5 and 8 will be written to output.txt

The result of output.txt is as follows:
```
[8, 15]
[8, 5]
[10]
```