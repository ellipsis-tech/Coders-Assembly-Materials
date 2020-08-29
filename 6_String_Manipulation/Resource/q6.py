# Name    :
# Email ID:

# start of answer
def strip_non_digits(value):
    return None # added so that this script will run. feel free to modify it

# end of answer

if __name__ == "__main__":
    print ('Test 1:')
    print ('Expected:12---600---0900---100-')
    result = strip_non_digits("12abc600$##0900AB 100X")
    print ('Actual  :' + result)
    print()

    print ('Test 2:')
    print ('Expected:34-5689---980')
    result = strip_non_digits("34.5689abc980")
    print ('Actual  :' + result)
    print()

    print('Test 3:')
    print('Expected:[---]')
    result = strip_non_digits("xyz")
    print('Actual  :[' + result + ']')
    print()

    print('Test 4:')
    print('Expected:---25')
    result = strip_non_digits("a-c25")
    print('Actual  :' + result)
    print()
