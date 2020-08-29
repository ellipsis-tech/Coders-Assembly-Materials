import q4 as qn

def sorted_output(phone_book):
    output = ''
    for key in sorted(phone_book):
        output += f"'{key}': '{phone_book[key]}', "
    
    return "{" + output[:-2] + "}"


print ('Test 1:')
print ("Expected:True")
result = qn.get_phone_book('q4-phone-book.txt')
print ('Actual  :' + str(isinstance(result,dict)))
print()

print ('Test 2:')
expected = {'George Leung-Mobile': '98987676', 'Eric Wong-Home': '67449908', 'Michelle Lee-Mobile': '96667777', 'Eric Wong-Mobile': '91234567', 'Michelle Lee-Pager': '88776655', 'Michelle Lee-Fax': '88776656'}
print ("Expected:" + sorted_output(expected))
result = qn.get_phone_book('q4-phone-book.txt')
print ('Actual  :' + str(sorted_output(result)))
print()

print ('Test 3:')
phone_book = {'George Leung-Mobile': '98987676', 'Eric Wong-Home': '67449908', 'Michelle Lee-Mobile': '96667777', 'Eric Wong-Mobile': '91234567', 'Michelle Lee-Pager': '88776655', 'Michelle Lee-Fax': '88776656'}
result  = qn.get_phone_numbers_for(phone_book, 'Eric Wong')
print ("Expected:True")
print ('Actual  :' + str(isinstance(result, dict)))
print()


print ('Test 4:')
phone_book = {'George Leung-Mobile': '98987676', 'Eric Wong-Home': '67449908', 'Michelle Lee-Mobile': '96667777', 'Eric Wong-Mobile': '91234567', 'Michelle Lee-Pager': '88776655', 'Michelle Lee-Fax': '88776656'}
result  = qn.get_phone_numbers_for(phone_book, 'Eric Wong')
expected = sorted_output({'Mobile': '91234567', 'Home': '67449908'})
print ("Expected:" + expected)
print ('Actual  :' + str(sorted_output(result)))
print()
