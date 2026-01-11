# loop control statement
# It is used to control the execution of loops.

# 1. pass statement

for i in range(5):
    # mann nhi hai
    pass

count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -=1

# 2. break statement

for i in range(10):
    if i == 5:
        break
    print(i)

# 3. continue statement

for i in range(10):
    if i == 3:
        continue
    print(i)

# count = 5
# while count > 0:
#     if count == 3:
#         # continue Infinite loop
#     else:
#         print(count)
#     count -=1

while True:
    user_input = input("Enter 'exit to stop:")
    if user_input == 'exit':
        print("congarts! you guesses it right")
        break
    print("sorry,you entered:", user_input)