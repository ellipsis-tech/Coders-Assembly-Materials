import q4 as qn

dictionary = qn.get_common_misspelling_dict('misspellings.txt')
result = qn.auto_correct_sentence("I sturddy at Singapore Managment Univercity", dictionary)
print('Test 1')
print('Expected:True')
print('Actual  :' + str(isinstance(result, str)))
print()

result = qn.auto_correct_sentence('I studdy Infomation Systems at Singapore Managment Unviersity', dictionary)
print('Test 2')
print('Expected:I study Information Systems at Singapore Management University')
print('Actual  :' + str(result))
print()


result = qn.auto_correct_sentence("Repatition is the mother of skill", dictionary)
print('Test 3')
print('Expected:Repetition is the mother of skill')
print('or')
print('Expected:Repartition is the mother of skill')
print('Actual :' + str(result))
print()