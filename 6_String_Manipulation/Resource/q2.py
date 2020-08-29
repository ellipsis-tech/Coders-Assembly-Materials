def count_num_vowels(sentence):
    pass

if __name__ == "__main__":
    print('Test 1')
    result = cal_avg_vowels_per_word(['apple', 'orange', 'durian'])
    print('Expected:3')
    print('Actual  :' + str(result))
    print()


    print('Test 2')
    result = isinstance(cal_avg_vowels_per_word(['apple', 'orange', 'durian']), int)
    print('Expected:True')
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    result = cal_avg_vowels_per_word(['apple'])
    print('Expected:2')
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    result = cal_avg_vowels_per_word(['by', 'sky', 'spy', 'try', 'gypsy', 'sly', 'sky', 'shy'])
    print('Expected:0')
    print('Actual  :' + str(result))
    print()

    print('Test 5')
    result = cal_avg_vowels_per_word([])
    print('Expected:0')
    print('Actual  :' + str(result))
    print()
