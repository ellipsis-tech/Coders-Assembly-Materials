# List and Tuple

### Q1
Implement the count words function. It takes in a parameter named `sentence` (type:`str`), and returns the number of words in the sentence. Test cases are provided for you in ql.py.

Use the `split` function. An example of using `split` function in the shell is provided below:
```
>>> 'a b c'.split()
['a', 'b', 'c']

>>> 'a b    c'.split()
['a', 'b', 'c']
```

### Q2
Implement a function called `get_long_strings()`. The function takes a list of strings (called `str_list`) as its parameter. The function returns the strings in the list that have at least 5 characters.

### Q3
Implement a function called get `longest_string()` . The function takes a list of strings (called `str_list`) as its parameter. The function returns the string in the list that has the maximum number of characters. if there are 2 longest strings, return the one with the smaller index (in the list).

### Q4
Implement a function called `get_cheapest_product()` . The function takes in 1 parameter, `product_list` (type: `list`). Each value is a tuple, and is of the format (name, price). Price is stated in cents. The function returns the cheapest product (i.e. minimum price) in the list. if there are 2 products with the same minimum price, return the one with the larger index (in the list).

### Q5
Implement a function called `count_odd_len()` . The function takes in 1 parameter, `str_list` (type: `list`). The function returns the number of strings whose length is odd.

### Q6
Examine code given to you below. Complete the function `get_numbers` to return a new list that contains only integers between min and max parameters. Your code should not modify the original list.

```
def get_numbers (num_list, min, max) :
#Write your functions get_numbers here




listl = [4, 10, 12, 28, 24, 18, 5, 20, 15, 21, 30, 22, 21, 14, 17, 28, 26, 24, 6, 8, 15]
new list = get_numbers(list1, 10, 20)

print("After function is called, original list:", list1)
print("After function is called, new list     :", new list)	
```

Expected output:
```
After function is called, original list: [14, 10, 12, 28, 24, 18, 5, 20, 15, 21, 30, 22, 21, 14, 17, 28, 26, 24, 6, 8, 15]
After function is called, new list     : [10, 12, 18, 20, 15, 14, 17, 15]
```

### Q7
Write a program that gets 10 integer inputs from the user. The program should then display the minimum, maximum and median of all numbers entered.

**Note:**  
The median is the middle of list of numbers. For example, median of numbers 12, 4, 5 is 5. In case of odd amount of numbers, the median is the exact middle number of numbers when arranged sorted.

In case of even amount of numbers, we would get a pair of middle numbers. The median is half way between them. As an example, median of numbers 5, 12, 4, 10 is 8 (6 + 10) 2 because when placed in order the middle numbers would be 6 and 10.

**Hint:**
1. This is how you can sort a list.
```
>>> numbers = [4, 10, 1, 3, -2] 
>>> numbers. sort()
>>> numbers
[-2, 1, 3, 4, 10]
```

Sample Run:
```
Enter num 1:-9 
Enter num 2:4 
Enter num 3:-11 
Enter num 4:19 
Enter num 5:5 
Enter num 6:17
Enter num 7:1 
Enter num 8:2 
Enter num 9:8 
Enter num 10:1
Minimum of numbers: -11 
Maximum of numbers: 19 
Median of numbers: 4.0
```

### Q8 *(Written Exercise)*
This exercise requires you to trace through the code. Guess the output of the following two programs and verify your answer by running the code.

(a)  
```
def funcl(strlist):
    str_list.append("durian")
    out = []
    for i in str_list:
        if len(i) > 5:
            out.append(i)
    return out


list1 = ["one", "apple", "six", "oranges", "bunch", "grapes"]
print ("Before function call:", list1)

#calling the function func1
new list = funcl(list1)
print("After function call:", list1)
print("New List	:", new_list)
```

(b)  
**Hint:**  
```
>>> li = [1, 2, 3] 
>>> li.insert(4)

>>> li
[1, 4, 2, 3]
```

While `append()` adds the element at the end of the list, `insert()` inserts the element before the index specified. List that contains another list inside is called a 2-dimensional list.  

```
def func2(list_2d):
    list_2d.insert (1, [7,8])
    new_list = list_2d[1:]
    new_list[1] = [10,11]
    return new_list

list1 = [[1,2], [3,4]]
list2 = [5,6]
listl.append(list2)

print ("Before function call:", list1)
list2 = func2(list1)
print ("After function call:", list1)
print ("List2 :", list2)
```

### Q9
Write a function called count numbers that takes in a list containing numbers and returns the count of numbers in the list. Your program has to cater to the possibility of having a list of numbers as element(s) in the input parameter. You can assume that the input parameter is at the most a 2-dimensional list.

<br>

Example 1: When the function is called as:
```
print ("Count of numbers", count_numbers([4, 6, 8, 10, -3]))
```

the expected output is:
```
Count of numbers:5
```

Example 2: When the function is called as:
```
print ("Count of numbers", count_numbers( [4, 6, [1,2] , 10, [-1 , -3] ] ) )
```

the expected output is:
```
Count of numbers:7
```
### Q10
Write a function called `merge_lists` that takes in 2 lists containing numbers and returns a new list containing all unique numbers present in the two lists sorted in the ascending order.

Example: When the function is invoked like this,
```
print ("Merging [1,2,3], [4,3,2]        :", merge_lists([1,2,3],[4,3,2])) 
print ("Merging [3,2,1], [2,6,4,10,4]   :", merge_lists([3,2,1],[2,6,4,10,4])) 
print ("Merging [3,1,1] , []            :", merge_lists ( [3,1,1] , [] ) )
print ("Merging [], [9,7,2,7]           :", merge_lists ( [] , [9,7,2,7] ) )
```

Expected output:
```
Merging [1,2,3], [4,3,2]      : [1, 2, 3, 4]
Merging [3,2,1], [2,6,4,10,4] : [1, 2, 3, 4, 6, 10]
Merging [3, 1,1] , []         : [1, 3] 
Merging [] , [9,7,2,7]        : [2, 7, 9] 
```

### Q11
Given the partial code as shown below, write the function called get_user_info that takes a list of email addresses and returns a list of tuples containing (user id, domain).  
Also, write the function print users that takes in the list of tuples and prints every user as a tuple.  
This exercise is adapted from the book "The Practice of Computing Using Python" Page 416, Exercise 45. The domain is the portion following @ sign in the email address.

```
#Write your functions get_user_info and print users here








name_list = ["shaun.chew.2010@sis.smu.edu.sg","sitongchen.2011@economics.smu.edu.sg"]
users_tuple = get_user_info(name_list)

print("Users and their domain")
print(users(users_tuple))
```

Sample Run:
```
Users and their domain
('lance.fu.2018', 'sis.smu.edu.sg') ('damianng.2018', 'economics.smu.edu.sg')
```

### Q12
Suppose you are out shopping, and you purchase 3 units of Product A (each of price $\$5.00$), 2 units of Product B (each of price $\$9.90$), and 1 unit of Product C (each of price $\$6.59$). We can represent this information using two lists:
- list of quantities of items purchased, e.g., `quantity_list = [3,2,1]`
- list of corresponding prices of items, e.g., `price_list = [5.00, 9.90, 6.59]`

The total amount of money that you have spent while shopping is thus given by: $3 * \$5 + 2 * \$9.90 + 1 * \$6.59 = \$41.39$. 

Write a Python function `compute_shopping_amount` which takes in two parameters `quantity_list` (containing list of quantities of items purchased) and `price_list` (containing corresponding list of prices of items), and returns the total amount spent. You may assume that the lengths of `quantity_list` and `price_list` will always be the same. You may assume that `quantity_list` will always contain valid integers, and `price_list` will always contain valid positive floating point numbers.

Sample output 1:
```
    quantity_list = [3,2,1], price_list = [5.00, 9.90, 6.59]
    distance = 41.39
```
Sample output 2:
```
    quantity_list = [4,5,7,1,2,10], price_list = [4.55, 23.8, 7.90, 3.40, 2.31, 8.78]
    shopping amount = 288.32
```

*Hint: Your solution should ideally not contain more than 5 lines of code, excluding the function definition and print statements.*

```
# print(compute_shopping_amount([3,2,1], [5.00, 9.90, 6.59]) == 41.39)
# print(compute_shopping_amount([4,5,7,1,2,10], [4.55, 23.8, 7.90, 3.40, 2.31, 8.78]) == 288.32)
```

### Q13
The [Manhattan Distance](https://www.mathworks.com/help/deeplearning/ref/mandist.html) 𝐷 between two vectors 𝑋 = {𝑥1 , 𝑥2 , ... , 𝑥𝑛} and 𝑌 = {𝑦1 , 𝑦2 , ... , 𝑦𝑛} is given by: 𝐷=∑<sup>𝑛</sup><sub>𝑖=1</sub>|𝑥𝑖−𝑦𝑖|.

It is also known as the [TaxiCab Metric](http://mathworld.wolfram.com/TaxicabMetric.html).

For instance, if 𝑋 = {1,4,10,5}  and 𝑌 = {5,2,8,5}, then the Manhattan Distance 𝐷 is given by: 
```
D = |1-5| + |4-2| + |10-8| + |5-5|
  = |-4| + |2| + |2| + |0| 
  = 4 + 2 + 2 + 0
  = 8
```
Note that |𝑎−𝑏| is equivalent to obtaining the absolute (i.e., positive) value of 𝑎−𝑏 . 

Write a Python function `compute_manhattan_distance` which takes in two parameters `X` (containing the list of $x$ values) and `Y` (containing the list of $y$ values), and returns the Manhattan Distance. If the lengths of 𝑋 and 𝑌 do not match, your function should display an error message that says `ERROR: Lengths of X and Y do not match!`, and then return `None`. You may assume that 𝑋 and 𝑌 are lists containing valid numbers. 

Sample output 1: 
```
    X = [1,4,10,5], Y = [5,2,8,5]
    distance = 8
```

Sample output 2: 
```
    X = [1,4,10,5,12,52], Y = [5,2,8,5,18]
    ERROR: Lengths of X and Y do not match!
```

*Hint: Your solution should ideally not contain more than 10 lines of code, excluding the function definition and print statements.*

```
# test your code 

# print(compute_manhattan_distance([1,4,10,5], [5,2,8,5]) == 8)
# print(compute_manhattan_distance([1,4,10,5,12,52], [5,2,8,5,18]) == None)
```

### Q14
Implement a function called `exchange_pairs()` . The function takes a `list` of strings, and switches the values pairwise: swap the value at index 0 with index 1, index 2 with index 3 and so on. If there is an odd number of values, the final value is not moved.

### Q15
mplement a function called `get_middle_items()` . The function takes a list of strings, and returns the word/words in the middle of the list.

### Q16
Implement a function called `calculate_variance()` . The function takes a parameter numbers (type: `list`), and returns the variance of a sample. Variance is the mean of the squares of the deviations from the arithmetic mean of a data set.

![variance](/asset/star2_wk7_q3.png)

**Reference:** https://www.wikihow.com/Calculate-Variance

### Q17
Implement a function called `combine_list()` . The function takes in two lists of values (`values1`, `values2`) and a boolean variable `is_remaining_front`. It merges the two lists by alternating between the two lists to take their values one by one and inserting these values into a new list. It then returns the new list. The two original lists should remain unchanged. If `is_remaining_front` is `True`, the remaining items will be appended in front. Otherwise, the remaining items will be appended behind.

<br>

Example 1:
```
valuesl : [ apple ' , ' orange , 'pear']
values2 : [1, 2, 3, 4, 5, 6, 7]
is_remaining_front : False
```

Returned value:
```
['apple' , 1, 'orange' , 2, 'pear , 3, 4, 5, 6, 7]
```

Example 2:
```
valuesl : [ ' apple	' orange ,'pear']
values2 : [1, 2, 3, 4, 5, 6, 7]
is_remaining_front : True
```

Returned value:
```
[4, 5, 6, 7, 'apple' , 1, 'orange' , 2, 'pear' , 3]
```

### Q18
Implement a function called `cumulative_sum()` . The function takes in a parameter, `numbers`. It then returns a list of numbers whereby `result[i]` in this list will be `numbers[0]` + `numbers[1]` + `numbers[2]` ... `numbers[i]`.

Example #1:
```
numbers :	[9, 1, 2, 5, 6]
```

Returned Value:
```
[9, 10, 12, 17, 23]
```

Note:  
1. `9 + 1 = 10`
2. `9 + 1 + 2 = 12`
3. `9 + 1 + 2 + 5 = 17`
4. `9 + 1 + 2 + 5 + 6 = 23`

### Q19
In mathematics, a transpose of a matrix is a new matrix whose rows are the columns of the original.

If matrix A is  

| 1        | 2        | 3        |
|----------|----------|----------|
| 4        | 5        | 6        |
| 7        | 8        | 9        |

The transpose of matrix A is (AT)

| 1        | 4        | 7        |
|----------|----------|----------|
| 2        | 5        | 8        |
| 3        | 6        | 9        |

Write a function called `transpose` that takes a 2D- list of numbers representing a square matrix (i.e. number of columns and rows are equal) and returns a transposed list. The original list should not be.

For the example shown above, the list representing the original would be `[ [1, 2,3] , [4,5, 6] , [7, 8, 9] ]`  
and the transposed list would be `[ [1, 4,7] , [2,5,8] , [3, 6, 9] ]`  

When the function is called like this:  
```
original = [[1,2],[3,4]]
print ("Original :", original)
print ("Transposed:", transpose(original)

original = [ [1,2,3], [4,5,6], [7,8, 9]]
print ( "Original : " , original )
print ("Transposed:", transpose(original) )
```

Expected output:
```
Original : [[1,	2], [3,	4]]
Transposed: [[1, 3], [2, 4]]
Original : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Transposed: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

Note:  
```
>>> list1 = [[1,2],[3,4]]
>>> list2 = list1.copy()
>>> list1 [0][0] = 9
>>> list1
[[9, 2], [3, 4]]
>>> list2
[[9, 2], [3, 4]]
```

We see from the above example that although we made a copy of `list1`, before making changes to lists, both `list1` and `list2` are changed. In order to make a proper copy of the 2d list, you could make use of copy module's `deepcopy()` method. This method makes a proper copy of the 2d list.

### Q20
In a magic square, every row, column and diagonal add up to the same total. Here is a 3 by 3 magic square. The numbers 1 to 9 are placed in the grid such that no number is repeated and the sum of three digits column-wise, row-wise and diagonal-wise is equal to 15

![magic square](/asset/2star_wk7_q7.png)

The elements of the above magic square can be represented using a 2-dimensional list. The above square is represented by `[ [ 4, 3, 8], [9, 5, 1] , [2, 7, 6] ]`.  

The following lists represent magic squares:

```
[4,3,8], [9,5,1], [2,7,6] ,
[4,9,2], [3,5,7], [8,1,6] ,
[6,1,8], [7,5,3], [2,9,4]
```

While the following do not:
```
[5,5,5], [5,5,5], [5,5,5] ,
[2,6,7], [9,5,1], [4,3,8] ,
[10,4,1], [1,5,9], [4,6,5]
```

<br>

Write a function is `magic_square()` that takes in a 2D list and returns `True` if the list contains all digits between 1 to 9 just once and if it forms a magic square, `False` otherwise. You can assume that a proper 3 by 3 - 2D list will be sent to the function.

Note: We suggest that you design the program to contain another function that checks if only numbers from 1 to 9 are present in the list and make use of that function in is magic square.

Here is the expected output (for the test cases shown above) :
```
[[4,3,8],[9,5,1],[2,7,6]] magic square?: True
[[4,9,2],[3,5,7],[8,1,6]] magic square?: True
[[6,1,8],[7,5,3],[2,9,4]] magic square?: True
[[5,5,5],[5,5,5],[5,5,5]] magic square?: False
[[2,6,7],[9,5,1],[4,3,8]] magic square?: False
[[10,4,1],[1,5,9],[4,6,5]] magic square?: False
```

### Q21
A sorting algorithm is an algorithm made up of a series of instructions that takes a list as input, performs specified operations on the list, and outputs a sorted list. This topic will be covered in depth in another course called "Computational Thinking".

Bubble sort is one of the simplest sorting algorithms that compares each pair of elements in a list swaps them if they are out of order until the entire list is sorted. For each element in the list, the algorithm compares every pair of elements.

Assume that you have the list `[7, 3, 6, 5, 1]`. In the first iteration, the adjacent elements are being compared to see if they are out of order. If there are n items in the list, then there are `(n - 1)` comparisons.

**First Pass:**  
![First Pass](/asset/2star_wk7_q8_1.png)

**Second Pass:**  
![Sec Pass](/asset/2star_wk7_q8_2.png)

![3rd and 4th Pass](/asset/2star_wk7_q8_3.png)

Implement the `bubble_sort()` function.

Reference: https://www.toptal.com/developers/sorting-algorithms:  
You can watch the animation here to compare the efficiency of various sorting algorithms.
