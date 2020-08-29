def get_cheapest_product(product_list):
    pass


if __name__ == "__main__":
    print('Test 1')
    str_list = [('apple', 70), ('orange', 80), ('pear', 60), ('durian', 1000)]
    result = get_cheapest_product(str_list)
    print("Expected:pear")
    print('Actual  :' + str(result))
    print()

    print('Test 2: Check data type')
    str_list = [('apple', 70), ('orange', 80), ('pear', 60), ('durian', 1000)]
    result = get_cheapest_product(str_list)
    print("Expected:<class 'str'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    str_list = [('apple', 70), ('orange', 80), ('pear', 60), ('banana', 60)]
    result = get_cheapest_product(str_list)
    print("Expected:banana")
    print('Actual  :' + str(result))
    print()

    print('Test 3')
    str_list = [('apple', 70)]
    result = get_cheapest_product(str_list)
    print("Expected:apple")
    print('Actual  :' + str(result))
    print()

    print('Test 4')
    str_list = []
    result = get_cheapest_product(str_list)
    print("Expected:None")
    print('Actual  :None')
    print()