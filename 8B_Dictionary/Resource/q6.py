def create_prime_dict(my_list):
    return

if __name__ == "__main__":
    print('\nTestcase 1')
    print('-' * 10)
    my_list = [2, 3, 5, 10, 20, 23]
    print("Expected: {2: True, 3: True, 5: True, 10: False, 20: False, 23: True}")
    print("Actual  : " + str(create_prime_dict(my_list)))

    print('\nTestcase 2')
    print('-' * 10)
    my_list = [4, 5, 6, 8, 11, 12]
    print("Expected: {4: False, 5: True, 6: False, 8: False, 11: True, 12: False}")
    print("Actual  : " + str(create_prime_dict(my_list)))