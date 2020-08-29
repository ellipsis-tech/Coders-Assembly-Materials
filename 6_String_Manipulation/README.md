# String Manipulation 

### Q1
Implement a function `count_num_vowels` that takes in a parameter, sentence. This function will return the number of vowels (i.e. the characters 'a', 'e' , 'o' and u') which 
can be uppercase or lowercase letters.

### Q2
Implement a function `cal_avg_vowels_per_word` that takes in a parameter, `word_list`. This function will return the average vowels per word in the `word_list`. Use the `round` function to return the average to the nearest whole number.

```
>>> round (12.1)
12
```

### Q3
Write a function called `reverse_words()` that takes in a string and returns a string where by all the words are reversed. For example, `reverse_words (apple orange pear durian' )` returns `durian pear orange apple` .

### Q4
Mobile numbers may sometimes be masked, to preserve privacy and minimze the possibility of spam. For instance, the first four digits of a mobile number 87654321 may be masked into xxxx4321. 

<img align="center" src="https://docs.google.com/uc?id=1DazBcIxawxC6E51DwHkAGgYflYDVUlj9" width="300"/>

<br>

Write a Python function `mask_mobile` that takes in a parameter `mobile_number` containing an 8-digit mobile number, and then returns the masked mobile number. You should not use any regex (regular expressions) in your solution. You may assume that the `mobile_number` is of 8 digits.  

Sample output 1:
```
    mobile_number = 87654321
    masked_number = xxxx4321
```

Sample output 2:
```
    mobile_number = 98765432
    masked_number = xxxx5432
```

*Hint: Your solution should ideally not contain more than 3 lines of code, excluding the function definition and print statements.*

```
# test your code 

# print((mask_mobile(87654321) == 'xxxx4321'))
# print((mask_mobile(98765432) == 'xxxx5432'))
```

#### Q5
An email address is typically of the format `local-part@domain`, where the local part may be up to 64 characters long and the domain may have a maximum of 255 characters. Email masking hides all or part of the local part of the email address; this is usually done to prevent bots from [harvesting email address](https://en.wikipedia.org/wiki/Email_address_harvesting) for spam or bulk emails. An example of a masked email address abcdef@gmail.com is given by ***@gmail.com.

Write a Python function `mask_email` that takes in a parameter `email_address` containing a *valid* email address, and then returns the masked email address. You should not use any regex (regular expressions) in your solution.  

Sample output 1: 
```
   email_address = abcdef@gmail.com
   masked_email = ******@gmail.com
```

Sample output 2: 
```
   email_address = smt111@smu.edu.sg
   masked_email = ******@smu.edu.sg
```

*Hint: Your solution should ideally not contain more than 3 lines of code, excluding the function definition and print statements.*

```
# test your code 

# print((mask_email('abcdef@gmail.com') == '******@gmail.com'))
# print((mask_email('smt111@smu.edu.sg') == '******@smu.edu.sg'))
```

### Q6
You are given q8.py. Implement a function called `strip_non_digits()` that will return a string with any non-digit replaced by the character '-'  

<br>

Example 1: If the function is invoked like this:  
```
print(strip_non_digits("12abc600$##0900AB100X"))
```

the statement generates the following output:
```
12---600---0900---100-
```

Example 2: If the function is invoked like this:  
```
print(strip_non_digits("34.5689abc980"))
```

the statement generates the following output:
```
34-5689---980
```

Example 3: If the function is invoked like this:  
```
print('[' + strip_non_digits("xyz") + ']')
```

the statement generates the following output:
```
[---]
```

Example 4: If the function is invoked like this:  
```
print(strip_non_digits("a-c25"))
```

The statement generates the following output:
```
---25
```