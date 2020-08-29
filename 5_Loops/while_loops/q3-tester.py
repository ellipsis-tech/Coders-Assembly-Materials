from q2 import calculate_average_length


print ('Test 1')
result = calculate_average_length([])
print ('Expected:True')
print ('Actual  :' + str(isinstance(result, float)))
print()

print ('Test 2')
result = calculate_average_length([])
print ('Expected:0.0')
print ('Actual  :' + str(result))
print()

print ('Test 3')
result = calculate_average_length(['', ''])
print ('Expected:0.0')
print ('Actual  :' + str(result))

print ('Test 4')
result = calculate_average_length(['James Gosling invented Java', 'Dennis Ritchie invented C', 'Microsoft developed C#', 'Guido van Rossum invented Python'])
print ('Expected:26.5')
print ('Actual  :' + str(result))


