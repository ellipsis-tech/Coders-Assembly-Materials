import q3 as qn

dictionary = qn.get_english_dictionary('words_alpha.txt')
result = qn.check_spelling("I sturddy at Singapore Managment Univercity", dictionary)
print('Test 1')
print ('Expected:True')
print ('Actual  :' + str(isinstance(result, list)))
print()

result = qn.check_spelling("I sturddy at Singapore Managment Univercity", dictionary)
print('Test 2')
print ('Expected:["sturddy", "Managment", "Univercity"]')
print ('Actual  :' + str(result))
print()