from q5 import get_students_of_age

print ('Test 1')
students = [('Mary','12/12/1980'), ('John', '1/12/1985'), ('Peter', '1/12/2015'), ('Christopher', '1/12/1945')]
result = get_students_of_age(students, 20, 45)
print("Expected:['Mary', 'John']")
print('Actual  :' + str(result))
print()

print ('Test 2')
students = [('Mary','12/12/1980'), ('John', '1/12/1985'), ('Peter', '1/12/2015'), ('Christopher', '1/12/1945')]
result = get_students_of_age(students, 30, 40)
print("Expected:<class 'list'>")
print('Actual  :' + str(type(result)))
print()


print('Test 3')
students = [('Bill', '1/12/1945'), ('Charles','12/12/1978'), ('Dill', '1/12/1988'),('Aries', '1/12/2015')]
result = get_students_of_age(students, 35, 75)
print("Expected:['Bill', 'Charles']")
print("Actual  :" + str(result))
print()

print('Test 4')
students = [('Charles','12/12/1978'), ('Dill', '1/12/1988'), ('Aries', '1/12/2015'), ('Bill', '1/12/1945')]
result = get_students_of_age(students, 65, 75)
print("Expected:['Bill']")
print("Actual  :" + str(result))
print()

print('Test 4')
students = []
result = get_students_of_age(students, 1, 5)
print("Expected:[]")
print("Actual  :" + str(result))
print()

