
def are_all_prices_higher_than(numbers, min_value):
    pass
    
if __name__ == "__main__":
    print('Test 1')
    result = are_all_prices_higher_than([1, 2, 9, 10, 12], 5)
    print("Expected:False")
    print("Actual  :" + str(result))
    print()

    print('Test 2: Check data type')
    result = are_all_prices_higher_than([1, 2, 5, 10, 12], 5)
    print("Expected:<class 'bool'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = are_all_prices_higher_than([5, 7, 10, 12], 5)
    print("Expected:False")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = are_all_prices_higher_than([9, 7, 10, 1], 5)
    print("Expected:False")
    print('Actual  :'  + str(result))
    print()

    print('Test 5')
    result = are_all_prices_higher_than([9, 7, 10], 5)
    print("Expected:True")
    print('Actual  :'  + str(result))
    print()

    print('Test 6')
    result = are_all_prices_higher_than([], 5)
    print("Expected:True")
    print('Actual  :'  + str(result))
    print()