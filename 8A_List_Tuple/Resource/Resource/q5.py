def count_odd_len(str_list):
    pass


if __name__ == "__main__":
    print('Test 1')
    str_list = ['apple', 'orange', 'pear']
    result = count_odd_len(str_list)
    print("Expected:1")
    print('Actual  :' + str(result))
    print()

    print('Test 2: Check data type')
    str_list = ['apple', 'orange', 'pear']
    result = count_odd_len(str_list)
    print("Expected:<class 'int'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    str_list = ['orange', 'durian', 'kiwi', 'banana', 'cherry']
    result = count_odd_len(str_list)
    print("Expected:0")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    str_list = ['mango', 'guava', 'apple', 'cherry', 'coconut']
    result = count_odd_len(str_list)
    print("Expected:4")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    str_list = []
    result = count_odd_len(str_list)
    print("Expected:0")
    print('Actual  :' + str(result))
    print()