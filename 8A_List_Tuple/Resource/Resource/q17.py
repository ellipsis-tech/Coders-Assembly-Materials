
numbers = [2, 4, 7, 3, 1, 9]
print(numbers[2:4])


if __name__ == "__main__":
    print('Test 1')
    result = cumulative_sum([9, 1, 2, 5, 6])
    print("Expected:[9, 10, 12, 17, 23]")
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    result = cumulative_sum([9, 1, 2, 5, 6])
    print("Expected:<class 'list'> <class 'int'>")
    print('Actual  :'  + str(type(result)) + ' ' + str(type(result[0])))
    print()

    print('Test 3')
    result = cumulative_sum([-1, 1, 2, 5, 6])
    print("Expected:[-1, 0, 2, 7, 13]")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = cumulative_sum([-1])
    print("Expected:[-1]")
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = cumulative_sum([])
    print("Expected:[]")
    print('Actual  :' + str(result))
    print()


