def is_gentle_number(number):
    pass


if __name__ == "__main__":
    print('Test 1')
    result = is_gentle_number(123)
    print('Expected:True')
    print('Actual  :' + str(result))
    print()


    print('Test 2')
    result = is_gentle_number(123)
    print('Expected:True')
    result = isinstance(result, bool)
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    result = is_gentle_number(2321235)
    print('Expected:False')
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = is_gentle_number(1)
    print('Expected:True')
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = is_gentle_number(0)
    print('Expected:None')
    print('Actual  :' + str(result))
    print()

    print('Test 6')
    result = is_gentle_number(-2)
    print('Expected:None')
    print('Actual  :' + str(result))
