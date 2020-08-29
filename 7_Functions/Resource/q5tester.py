from q4 import get_numbers_containing_digit

print('Test 1')
print('Expected:[1, 123, 213, 321]')
result = get_numbers_containing_digit([1,123,213,321, 4, 456], 1)
print('Actual  :' + str(result))
print()

print('Test 2')
print("Expected:<class 'list'>")
result = get_numbers_containing_digit([1,123,213,321, 4, 456], 1)
print('Actual  :' + str(type(result)))
print()

print('Test 3')
print('Expected:[]')
result = get_numbers_containing_digit([2,234,23,32, 4, 456], 1)
print('Actual  :' + str(result))
print()

print('Test 4')
print('Expected:[12, 4561]')
result = get_numbers_containing_digit([12,234,23,32, 4, 4561], 1)
print('Actual  :' + str(result))
print()

print('Test 5')
print('Expected:[]')
result = get_numbers_containing_digit([], 1)
print('Actual  :' + str(result))
print()

print('Test 6')
print('Expected:[-22133]')
result = get_numbers_containing_digit([-22133], 1)
print('Actual  :' + str(result))
print()
