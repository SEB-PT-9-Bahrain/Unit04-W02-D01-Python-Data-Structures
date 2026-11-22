# Lists

students = ['Ammar','Abdullah','Ahmed']

# Accessing values by index
print(students[2])

# Python also supports negative index
print(students[-2])


# len() same as .length
print(len(students))

# append(): adds an element at the end of the List
students.append('Mohammed')

print(students)

# pop(): removes the last element
students.pop()

print(students)


# pop(1): removes the value at the index position 1
students.pop(1)

print(students)

# pop(0): remove the first element in the List

# extend(): adds many values to the end of the List
students.extend(['Sayed Baqer','Sayed Ali','Yusef'])

print(students)

# insert(index, value): will add the value at the index
students.insert(3,'Amir')
print(students)

# insert(0, value): Adds value to the beggening of List


students.clear()


print(students)

students.extend(['Sayed Baqer','Sayed Ali','Yusef'])

print(students)


for one_student in students:
    print(one_student)


print(tuple(enumerate(students)))

for index, one_student in enumerate(students):
    print(f'{one_student} is at index {index}')

# Tuple: unchanging list

flag_colors = ('White','Red')

# flag_colors[0] = 'Blue'
print(flag_colors[0])


students.extend(['Ammar','Abdullah','Ahmed'])
# Slice
# 0 to 2 (NOT INCLUDING 2)

print(students)
print(students[0:3])

# go from 2 until the end
print(students[2:])


print(students[:])


print(students[1:5:3])


print(students[0::2])
print(students[:4:6])

print('---------------')
# Dictionary

ga_student = {
    "name":"Ammar",
    "course":"SEB",
    "favorite_language":"Angular"
}


print(ga_student['favorite_language'])

# editing a key value pair
ga_student['favorite_language'] = 'Python'

print(ga_student)

# Add a new key value pair
ga_student['cpr_number'] = 8793679653479


print(ga_student)

# deletes a key value pair
del ga_student['course']


print(ga_student)


for key, value in ga_student.items():
    print(f'{key} ----> {value}')