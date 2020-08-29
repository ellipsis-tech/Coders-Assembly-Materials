# Top-Down Design
# This may be a problem that is too complicated to solve by one function alone.
# 1. Try breaking the problem down into sub-problems. Each sub-problem is a helper function.
# 2. To identify a sub-problem, start writing the algorithm out. 
# 3. When you get to a step that seems too complicated, imagine you have a helper function that can solve that step.
#    See if you can write the function by including a call to this imaginary function, 
# 4. The process can then be repeated on the helper functions until the solution is complete.


if __name__ == "__main__":
    print('Test 1')
    result = calculate_variance([17, 15, 23, 7, 9, 13])
    print("Expected:33.2")
    print('Actual  :' + str(result))
    print()

    print('Test 2')
    result = calculate_variance([17, 15, 23, 7, 9, 13])
    print("Expected:<class 'float'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = calculate_variance([])
    print("Expected:<class 'float'>")
    print('Actual  :' + str(type(result)))
    print()

    print('Test 3')
    result = calculate_variance([])
    print("Expected:0.0")
    print('Actual  :' + str(result))
    print()