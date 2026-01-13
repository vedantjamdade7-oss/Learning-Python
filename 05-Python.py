# OPERATORS

#  1. Arithmetic operators
a = 8
b = 4
print(a+b) # Addition operator
print(a-b) # substraction operator
print(a*b) # multiplication operator
print(a/b) # Division opertor
print(a%b) # modulus opertor

# 2. comparision operator
a = 10
b = 7
print(a>b) #Greater than operator
print(a<b) #less than operator
print(a==b) # equal 
print(a!=b) # not equal 

# 3. Assingment operator
a = 10 # assingment operator

# 4. Logical operator
# Rule for 'and' operator
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False

a = 10
b = 20
print(a>10 and b<10) #and operator
print(a==10 and b==20)
print(a==10 or b<10) # or operator

# Rule of 'or' operator
# True + False = True

# 'not' operator
print(not(a==10 and b==20))

# 5. Identity operator -is , is not
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y) # is operator
print(x is z)

print(x is not z) # is not operator

# 6.Membership operator-in, not in
my_list = ["apple","orange","mango"]
print("apple" in my_list) # in
print("watermelon" in my_list)

print("apple" not in my_list) # not in 

# 7. bitwise operator - And &, OR |, XOR ^, NOT ~, etc

# Rule for '&' operator
# 1. True(1) + True(1) = True(1)
# 2. True(1) + False(0) = False(0)
# 3. False(0) + False(0) = False(0)

a = 5        # 5 in binary - 0101
b = 3        # 3 in binary - 0011
print(a & b) # 1 in binary - 0001