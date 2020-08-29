def get_ordinal_number(number):
    pass

if __name__ == "__main__":
    print('Test 1')
    print('Expected:0th')
    print('Actual  :' + get_ordinal_number(0))
    print()

    print('Test 2')
    print('Expected:True')
    result = isinstance(get_ordinal_number(0), str)
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    print('Expected:1st')
    print('Actual  :' + get_ordinal_number(1))
    print()

    print('Test 4')
    print('Expected:2nd')
    print('Actual  :' + get_ordinal_number(2))
    print()

    print('Test 5')
    print('Expected:3rd')
    print('Actual  :' + get_ordinal_number(3))
    print()

    print('Test 6')
    print('Expected:4th')
    print('Actual  :' + get_ordinal_number(4))
    print()

    print('Test 7')
    print('Expected:11th')
    print('Actual  :' + get_ordinal_number(11))
    print()

    print('Test 8')
    print('Expected:12th')
    print('Actual  :' + get_ordinal_number(12))
    print()


    print('Test 9')
    print('Expected:13th')
    print('Actual  :' + get_ordinal_number(13))
    print()

    print('Test 10')
    print('Expected:21st')
    print('Actual  :' + get_ordinal_number(21))
    print()

    print('Test 11')
    print('Expected:111th')
    print('Actual  :' + get_ordinal_number(111))
    print()

    print('Test 12')
    print('Expected:121st')
    print('Actual  :' + get_ordinal_number(121))
    print()

    print('Test 13')
    print('Expected:-1')
    print('Actual  :' + get_ordinal_number(-1))
    print()
