def reverse_words(sentence):
    pass

if __name__ == "__main__":
    print('Test 1')
    print('Expected:pear orange apple')
    print('Actual  :' + reverse_words('apple orange pear'))
    print()


    print('Test 2')
    print('Expected:you worry me')
    print('Actual  :' + reverse_words('me worry you'))
    print()

    print('Test 3')
    print('Expected:test')
    print('Actual  :' + reverse_words('test'))
    print()

    print('Test 3')
    print('Expected:[]')
    print('Actual  :[' + reverse_words('') + ']')
    print()
