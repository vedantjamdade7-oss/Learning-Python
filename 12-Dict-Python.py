# Dictionary in python
# This is used to store data in key:value pair. It is unordered and mutable.

# syntax: dict = {'key1':'value1', 'key2':'value2',.......}

student = {
    "name": "Vedant",
    "age": 20,
    "course": "Pyhton"
}

print(student)
print(type(student))


# Access Dictionary value - This is done by using key name inside square brackets [] or by using get() method also.
# The access is used to get value of particular key.
student = {
    1:"class-x",
    'name':'vedant',
    'age': 20,
    'city':'nagpur'
 }

print(student['name'])
print(student['age'])
print(student['city'])
print(student[1])