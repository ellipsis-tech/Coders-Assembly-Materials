def count_words(sentence):
    pass

if __name__ == "__main__":
    print('Test 1')
    print('Expected:6')
    result = count_words('The cat jumps over the wall')
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    print('Expected:True')
    result = isinstance(count_words('The cat jumps over the wall'), int)
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    print('Expected:1')
    result = count_words('The ')
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    print('Expected:0')
    result = count_words('  ')
    print('Actual  :' + str(result))
    print()
