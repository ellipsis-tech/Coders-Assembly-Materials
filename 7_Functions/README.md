# Functions

### Q1
Implement the `isprimenumber` function. A prime number is a whole number greater than 1 whose only factors are 1 and itself. A factor is a whole numbers that can be divided evenly into another number. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.

### Q2
Implement a function `are_all_prices_higher_than`. It takes in two parameters: `numbers` and `min_value`, and returns `True` if all the values in numbers are greater than the `min_value`. Otherwise, this function returns `False`.

### Q3
Implement the `is_gentle_number` function. A gentle number is a positive number where all its adjacent digits differ by only 1. For example, the number 876. The digits 8 and 7 differ by 1, and the digits 7 and 6 differ by 1. All single digit numbers are considered gentle numbers.

#### Q4
Write a function `get_ordinal_number` that takes in a parameter number (type: `int`). If the number is greater than or equal to 0, this function returns a string of the number followed by the ordinal suffix est', 'nd', 'rd', 'th'). For example,
- get ordinal number (0) will return the value 0th.
- get ordinal number (1) will return the value 1st.
- get ordinal number (2) will return the value 2nd.
- get ordinal number (3) will return the value 3rd.
- get ordinal number (4) will return the value 4th.

Otherwise, the function will just return the original value without any suffix. The logic to decide on the ordinal suffix is as follows:

|Number ends with|Suffix|
|:---------------|:-----|
|11, 12 or 13|th|
|1|st|
|2|nd|
|3|rd|
|Everything else|th|

<br>

**Reference**: https://en.wikipedia.org/wiki/Ordinal_indicator#Other_suffixes

### Q5
implement a function called get _numbers_containing_digit. This function takes in two parameters:

1. `number_list` (type: `list`): `number_list` is a list of numbers (type: `int`)
2. `digit` (type:`int`): an integer whose value is between 0(inclusive) and 9 (inclusive).

This function returns the numbers in `number_list` that contains at least one occurrence of the specified `digit`.

### Q6
Implement the function called get students_ of_ age. This function takes three parameters:

1. `student_list` (type: `list`) : Each value is a tuple, and is of the format (name, birthday) where birthday is in day/month/year format.
2. `low` (type: `int`) : This is the lower bound of age.
3. `high` (type: `int`): This is the upper bound of age.

The function returns a list that contains the name of all students whose age(current year - birth year) is between low (inclusive) and high (inclusive) from `student_list`.

```
>>> import datetime
>>> now = datetime.datetime.now()
>>> print(now.year, now. month, now. day) 
2018 10 15
```
