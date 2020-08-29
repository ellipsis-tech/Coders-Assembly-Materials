import q5 as qn

print ('Test 1')
result = qn.reverse({'Billy':41, 'Charlie':54, 'Alfred':81, 'Elise':61, 'Daniel':41})
print ('Expected:True')
print ("Actual  :" + str(isinstance(result[41], list)))
print ()

print ('Test 2')
result = qn.reverse({'Billy':41, 'Charlie':54, 'Alfred':81, 'Elise':61, 'Daniel':41})
print("Expected:{41: ['Billy', 'Daniel'], 54: ['Charlie'], 81: ['Alfred'], 61: ['Elise']}")
print("Actual  :" + str (result))
