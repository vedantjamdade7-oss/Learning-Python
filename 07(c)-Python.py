# Nested loop - is a loop inside another loop.

# syntax:
# outer_loop:
    # inner_loop:
        # block of code inner loop
# block of code for outer loop

# print number from 1 to 3

for i in range(3):
    for num in range(1,4):
        print(num)
    print('- - -')
