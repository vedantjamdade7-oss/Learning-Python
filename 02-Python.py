# Data type in python
# Data types are the classification or categorization of data items.
a = 1
b = 1
print(a+b)
print(type(a)) # checking data type: integer

c = "1"
d = "1"
print(c+d)
print(type(c)) # checking data type: string

# Basic data types in python
a1 = 1            # 1a.integer
a2 = 1.5          # 1b.flot
print(type(a2))

a3 = complex(3,5) #1c.complex
print(type(a3))


#2.sequence
b1 = "vedant" 
print(type(b1)) # string

b2 = [1,2,3,4,"vedant","karan"] # list
print(type(b2))

b3 = (1,2,3,4,"vedant","karan") # tuple
print(type(b3))

#3.Dictionary
# Key Value pare 
myname = {'name':'vedant','age':20,'city':'nagpur'}
print(type(myname))

#4. Set
mysets = {1,2,3,4,"vedant","karan"}
print(type(mysets))

#5.Boolean
bool1 = True
bool2 = False
print(type(bool1))

#6.Binary
# bytes,bytearray,memoryview
byte1 = b"Madhav"
print(type(byte1))