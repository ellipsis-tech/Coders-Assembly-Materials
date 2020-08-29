def get_middle_items(values):
    pass

if __name__ == "__main__":
    print('Test 1')
    str_list = ['apple', 'orange', 'pear', 'durian']
    result = get_middle_items(str_list)
    print("Expected:['orange', 'pear']")
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    str_list = ['apple', 'orange', 'guava', 'pear', 'durian']
    result = get_middle_items(str_list)
    print("Expected:['guava']")
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    str_list = ['apple', 'orange']
    result = get_middle_items(str_list)
    print("Expected:['apple', 'orange']")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    str_list = ['apple']
    result = get_middle_items(str_list)
    print("Expected:['apple']")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    str_list = []
    result = get_middle_items(str_list)
    print("Expected:[]")
    print('Actual  :' + str(result))
    print()