#  Module and Package in Python
# 1️. What is a Module in Python?

# A module is a single Python file (.py) that contains functions, classes, or variables.
# It allows you to organize your code into separate files for better maintainability and reusability.

# Example:-
# Let's say we have a module named 'calculator.py' with the following content:
# calculator.py (This is a module)
# calulator.py (This is a module)

# def add(a, b): This part is new in the recent edit
#     return a+b

# def subtract(a, b): 
#     return a - b

# def multiply(a, b):
#     return a * b

# 2. Importing a Module
# you can import a module into your python script using the "import" statement.

import calculator

print(calculator.add(5, 3))
print(calculator.subtract(10, 4))

