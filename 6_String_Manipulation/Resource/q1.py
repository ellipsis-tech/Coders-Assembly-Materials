def count_num_vowels(sentence):
    pass

if __name__ == "__main__":
    print('Test 1')
    result = count_num_vowels('The brown fox jumps over the wall')
    print('Expected:8')
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    result = isinstance(count_num_vowels('The brown fox jumps over the wall'),int)
    print('Expected:True')
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    result = count_num_vowels('Tht wld nt b pssbl. Nglsh wrds mst hv vwls.')
    print('Expected:0')
    print('Actual  :' + str(result))


    print('Test 4')
    result = count_num_vowels('')
    print('Expected:0')
    print('Actual  :' + str(result))
