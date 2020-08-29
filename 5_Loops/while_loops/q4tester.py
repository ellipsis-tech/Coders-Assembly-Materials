from q3 import last_index_of

print ('Test 1')
print ('Expected:-1')
result = last_index_of([], 3)
print ('Actual  :' + str(result))
print()

print ('Test 2')
print ('Expected:1')
result = last_index_of([3, 5, 7], 5)
print ('Actual  :' + str(result))
print ()

print ('Test 3')
print ('Expected:3')
result = last_index_of([3, 5, 7, 5, 4], 5)
print ('Actual  :' + str(result))
print ()
