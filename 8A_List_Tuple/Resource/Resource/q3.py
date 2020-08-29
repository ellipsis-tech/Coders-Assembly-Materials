def get_longest_string(str_list):
    pass


if __name__ == "__main__":
    print('Test 1')
    str_list = ['apple', 'orange', 'pear']
    result = get_longest_string(str_list)
    print("Expected:orange")
    print('Actual  :' + str(result))
    print()

    print('Test 2: Check data type')
    str_list = ['apple', 'orange', 'pear']
    result = get_longest_string(str_list)
    print("Expected:<class 'str'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = get_longest_string(['', 'SMU', 'S I S'])
    print("Expected:S I S")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = get_longest_string(['apple', 'durian', 'orange'])
    print("Expected:durian")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = get_longest_string([])
    print("Expected:None")
    print('Actual  :' + str(result))
    print()

    print('Test 6')
    result = get_longest_string([''])
    print("Expected:[]")
    print('Actual  :[' + str(result) + ']')
    print()
