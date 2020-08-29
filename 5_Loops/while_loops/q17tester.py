from q6 import generate_initials

print('Test 1')
result = generate_initials(['Lily TAN', 'Ilse Corina Ee'])
print("Expected:[('LT', 'Lily TAN'), ('ICE', 'Ilse Corina Ee')]")
print('Actual  :' + str(result)) 
print()

print('Test 2')
result = generate_initials(['Lily TAN', 'Ilse Corina Ee'])
print("Expected:<class 'list'>")
print('Actual  :' + str(type(result)))
print()

print('Test 3')
result = generate_initials(['Lily TAN', 'Ilse Corina Ee'])
print("Expected:<class 'tuple'>")
print('Actual  :' + str(type(result[0])))
print()

print('Test 4')
result = generate_initials(['Alvin LIN Jun Jie', 'Kelvin'])
print("Expected:[('ALJ', 'Alvin LIN Jun Jie'), ('KE', 'Kelvin')]")
print('Actual  :' + str(result)) 
print()

print('Test 5')
result = generate_initials(['Amy LIM', 'Lucy TAN', 'Lily Tang', 'Lesley TOH', 'Lucase TEO'])
print("Expected:[('AL', 'Amy LIM'), ('LT', 'Lucy TAN'), ('LT2', 'Lily Tang'), ('LT3', 'Lesley TOH'), ('LT4', 'Lucase TEO')]")
print('Actual  :' + str(result)) 
print()

print('Test 6')
result = generate_initials(['Kelvin', 'Kenny', 'Kenneth', 'Kevin', 'TAN Bai Hua', 'TAN Beh Hong'])
print("Expected:[('KE', 'Kelvin'), ('KE2', 'Kenny'), ('KE3', 'Kenneth'), ('KE4', 'Kevin'), ('TBH', 'TAN Bai Hua'), ('TBH2', 'TAN Beh Hong')]")
print('Actual  :' + str(result)) 
print()

