# Dictionary

## Q1
Write a function `has_same_value` that accepts two dictionaries, `dl` and `d2` and a str named `key`. It returns True if the key is found in both dictionaries and the key has the same value. Otherwise, this function returns False. You are given `ql-tester.py`.


## Q2
Write the q2.py program: This program will keep prompting the user for words until the user enters an empty string. Your program is supposed to note down the frequency of words entered. The program then keeps prompting the user for a word and print outs the frequency of the word, until such word is prompted that is not found(not previously entered by the user).
```
D:\IS111>python q2.py
Enter the word>apple 
Enter the word>apple 
Enter the word>orange 
Enter the word>pear 
Enter the word>orange 
Enter the word>pear 
Enter the word>pear 
Enter the word>

Enter query word>orange
2

Enter query word>pear
3

Enter query word>banana 
Not found.
Bye bye
```

## Q3

"A __substitution cipher__ is a method of encoding by which units of plaintext are replaced with ciphertext, according to a fixed system." See https://en.wikipedia.org/wiki/Substitution_cipher.

In this question, we consider a simple substitution cipher that replaces each letter in the original message with another letter.

### Part (a)

You are given a dictionary that stores the mappings from English lowercase letters to their replacements. Note that no two letters will be mapped to the same replacement.

Define a function called `encrypt()` that takes in two parameters:

- `my_dict` (type: `dict`): a dictionary as described above. 
- `msg` (type: `str`): a message consisting of only lowercase letters and spaces.

The function returns the encrypted message using `my_dict` as the substitution cipher. Note that a space remains untouched in the encrypted message.

```
# Test cases used to test your function

cipher_dict = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

print('\nTestcase')
print('-' * 10)
print("Expected: v ybir clguba")
msg = 'i love python'
print("Actual  : " + encrypt(cipher_dict, msg))
```
### Part (b)

Now define a function called `decrypt()`. This function also takes in two parameters:

- `my_dict` (type: `dict`): a dictionary as described above. 
- `encrypted_msg` (type: `str`): an __encrypted__ message.

The function returns the original message, i.e., the message that has been encrypted into the string `encrypted_msg`.
```
cipher_dict = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

print('\nTestcase')
print('-' * 10)
msg = 'v ybir clguba'
print("Expected: i love python")
print("Actual  : " + decrypt(cipher_dict, msg))
```

## Q4

You are given a file called `q4-tester.py`. Define the following functions in `q4.py`:

(a) `get_common_misspelling_dict()`: The function takes in a filename and returns a dictionary where the key is the misspelled word (e.g. ithast'), value is the list of corrected word (e.g. ["that", "that's"]). The file `misspellings.txt` contains one word per line. Do remember to remove the spaces from both ends and the trailing end of line character. If the file contains:
```
adressed-> addressed
adressing-> addressing, dressing
```
This method will return the following `dict` object:
```
{'adressed': ['addressed'] , 'adressing': [addressing', 'dressing']}
```
**Note:** You are given misspellings.txt.

(b)`auto_correct_sentence()`: The function takes in a sentence and returns a list of words from the sentence correcting possibly misspelled words, i.e., a list of words that are not found in the English dictionary. For example, auto_correct_sentence('I studdy Infomation Systems at Singapore Managment University') should return 'I study Information Systems at Singapore Management University'. If the first character of the misspelled word is capitalized, you should capitalize the first character of the misspelled word too.

If there is more that one possible correct words, then randomly pick one of the words. For example, "thast" is a mis-spelling of either "that" or "that's". Therefore, the answer for "Thast a good one" can either be "That a good one" or "That's a good one".

**Reference**: https://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines


## Q5
You are given a file called `q5-tester.py`. Write a function called **reverse** in `q5.py` that accepts a dictionary of strings mapped to strings as parameter and returns a new map that is the reverse of the original. The reverse of a dictionary is a new dictionary that uses the values from the original as its keys and the keys from the original as its values. Since a dictionary's values need not be unique but its keys must be, you will have each value mapped to a List of keys. For example, if the input parameter map consists of the following
| Key(person's name) | Value(Quiz Score) |
| ----------- | ----------- |
| Alfred      | 81       |
| Elise       | 61       |
| Billy       | 41       |
| Daniel      | 41       |
| Charlie     | 54       |

The return value of the method should be a dictionary consisting of the following:
| Key(Quiz Score) | Value(person's name) |
| ----------- | ----------- |
| 41      | Billy, Daniel   |
| 61       | Elise          |
| 81       | Alfred         |
| 54      | Charlie         |

(The order of the keys and values does not matter.) 

## Q6 
Define a function called ```create_prime_dict()``` that takes in a list of integers greater than 1 (without any duplicates) as its parameter. The function creates a dictionary that maps each integer in the list to a boolean value that indicates whether or not this integer is a prime number.

Recall that a prime number is a number that is divisible only by 1 and itself.

For example, ```create_prime_dict([2, 3, 5, 10, 20, 23])``` returns a dictionary that looks like the following: ```{2:True, 3:True, 5:True, 10:False, 20:False, 23:True}```.

```
print('\nTestcase 1')
print('-' * 10)
my_list = [2, 3, 5, 10, 20, 23]
print("Expected: {2: True, 3: True, 5: True, 10: False, 20: False, 23: True}")
print("Actual  : " + str(create_prime_dict(my_list)))

print('\nTestcase 2')
print('-' * 10)
my_list = [4, 5, 6, 8, 11, 12]
print("Expected: {4: False, 5: True, 6: False, 8: False, 11: True, 12: False}")
print("Actual  : " + str(create_prime_dict(my_list)))
```
## Q7

You are given a file called "facilities.txt" that stores the information of some facilities in SMU. Each line of the file contains the following columns of information, separated by tabs.

```
school    room_number    capacity    has_projector
```

Note that different schools may have the same room number. For example, both SIS and SOE may have an MR-5.1. But within each school the room numbers are unique.


Write a program that allows a user to continuously check the details of a room until the user chooses to quit the program.

A sample run of the program may look like the following:

```
Do you want to search for a facility? [Y|N] :Y
Enter the school [LKCSB|SOE|SOL|SOA|SIS] :SOE
Enter the room number :SR-3.1
SOE SR-3.1 has a capacity of 50 and has a projector.

Do you want to continue the search? [Y|N] :Y
Enter the school [LKCSB|SOE|SOL|SOA|SIS] :SIS
Enter the room number :MR-4.3
SIS MR-4.3 has a capacity of 15 and does not have a projector.

Do you want to continue the search? [Y|N] :Y
Enter the school [LKCSB|SOE|SOL|SOA|SIS] :SIS
Enter the room number :SR-3.1
SIS SR-3.1 has a capacity of 60 and has a projector.

Do you want to continue the search? [Y|N] :N
Thanks for using our system!
```