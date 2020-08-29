import q1 as qn

d1 = {'apple':1, 'orange': 2}
d2 = {'durian':1, 'orange': 2}
print ('Test 1:check return value is of bool type')
result = qn.has_same_value(d1, d2, 'apple')
print ('Expected:True')
print ('Actual  :' + str(isinstance(result, bool)))
print()

d1 = {'apple':1, 'orange': 4}
d2 = {'durian':1, 'orange': 4}
print ('Test 2: key does not exists in both')
result = qn.has_same_value(d1, d2, 'durian')
print ('Expected:False')
print ('Actual  :' + str(result))
print()


d1 = {'apple':1, 'orange': 2}
d2 = {'durian':1, 'orange': 2}
print ('Test 3: key only exists in one dictionary')
result = qn.has_same_value(d1, d2, 'apple')
print ('Expected:False')
print ('Actual  :' + str(result))
print()


d1 = {'apple':1, 'orange': 2}
d2 = {'durian':1, 'orange': 3}
print ('Test 4: key exists but values are different')
result = qn.has_same_value(d1, d2, 'orange')
print ('Expected:False')
print ('Actual  :' + str(result))
print()

d1 = {'apple':1, 'orange': 4}
d2 = {'durian':1, 'orange': 4}
print ('Test 5: key exists and values are the same')
result = qn.has_same_value(d1, d2, 'orange')
print ('Expected:True')
print ('Actual  :' + str(result))
print()
