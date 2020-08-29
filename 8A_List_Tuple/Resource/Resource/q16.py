

if __name__ == "__main__":
    print('Test 1')
    result = combine_list([1,2,3], ['apple', 'orange', 'pear'], False)
    print("Expected:[1, 'apple', 2, 'orange', 3, 'pear']")
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    result = combine_list([1,2,3], ['apple', 'orange', 'pear'], False)
    print("Expected:<class 'list'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = combine_list([1,2,3], ['apple', 'orange', 'pear'], True)
    print("Expected:[1, 'apple', 2, 'orange', 3, 'pear']")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = combine_list([1,2,3], ['apple', 'orange', 'pear', 'durian'], True)
    print("Expected:['durian', 1, 'apple', 2, 'orange', 3, 'pear']")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = combine_list([1,2,3], ['apple', 'orange', 'pear', 'durian'], False)
    print("Expected:[1, 'apple', 2, 'orange', 3, 'pear', 'durian']")
    print('Actual  :' + str(result))
    print()

    print('Test 6: Corner Case #1')
    result = combine_list([], ['apple', 'orange', 'pear', 'durian'], False)
    print("Expected:['apple', 'orange', 'pear', 'durian']")
    print('Actual  :' + str(result))
    print()

    print('Test 7: Corner Case #2')
    result = combine_list(['apple', 'orange', 'pear', 'durian'], [], False)
    print("Expected:['apple', 'orange', 'pear', 'durian']")
    print('Actual  :' + str(result))
    print()


    print('Test 7: Corner Case #3')
    result = combine_list([], [], False)
    print("Expected:[]")
    print('Actual  :' + str(result))
    print()