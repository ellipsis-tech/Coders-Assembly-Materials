def exchange_pairs(str_list):
    pass

if __name__ == "__main__":
    print('Test 1')
    str_list = ['apple', 'orange', 'pear', 'durian']
    exchange_pairs(str_list)
    print("Expected:['orange', 'apple', 'durian', 'pear']")
    print('Actual  :' + str(str_list))
    print()


    print('Test 2')
    str_list = ['apple', 'orange', 'pear', 'durian', 'guava']
    exchange_pairs(str_list)
    print("Expected:['orange', 'apple', 'durian', 'pear', 'guava']")
    print('Actual  :' + str(str_list))
    print()

    print('Test 3')
    str_list = []
    exchange_pairs(str_list)
    print("Expected:[]")
    print('Actual  :' + str(str_list))
    print()