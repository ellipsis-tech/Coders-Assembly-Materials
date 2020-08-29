def get_long_strings(str_list):
    pass

if __name__ == "__main__":
    print('Test 1')
    str_list = ['apple', 'orange', 'pear']
    result = get_long_strings(str_list)
    print("Expected:['apple', 'orange']")
    print('Actual  :' + str(result))
    print()
    print("Expected:['apple', 'orange', 'pear']")
    print('Actual  :' + str(str_list))
    print()

    print('Test 2: Check data type')
    str_list = ['apple', 'orange', 'pear']
    result = get_long_strings(str_list)
    print("Expected:<class 'list'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = get_long_strings(['', 'SMU', 'S I S'])
    print("Expected:['S I S']")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = get_long_strings([''])
    print("Expected:[]")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = get_long_strings([])
    print("Expected:[]")
    print('Actual  :' + str(result))
    print()