# Operators in Python are symbols that perform operations on variables and values.
# 7 types in python

# 1 - ARITHMETIC OPERATORS:  used for mathematical calculations.
# Addition
x = 5 + 3

# Subtraction
y = 10 - 4

# Multiplication
z = 2 * 5  

# Division (float division)
w = 15 / 3  

# Integer Division (Floor Division / integer division)
q = 15 // 4  

# Modulus (Remainder)
r = 15 % 4  



# 2 - COMPARISON OPERATORS - used to compare values and return True or False

x = 5
y = 10

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Greater than
print(x > y)  # False

# Less than
print(x < y)  # True

# Greater than or equal to
print(x >= y)  # False

# Less than or equal to
print(x <= y)  # True



# 3 - LOGICAL OPERATORS - used to combine conditional statements and evaluate multiple conditions
x = 5
y = 10

# AND operator
print(x < 10 and y > 5)  # True (both conditions are True)

# OR operator
print(x < 10 or y < 5)  # True (at least one condition is True)

# NOT operator
print(not(x < 10 and y > 5))  # False (negation of True is False)


# 4 - ASSIGNMENT OPERATORS - used to assign values to variables
# they include the basic assignment operator '=' as well as compound assignment operators that combine arithmetic operations with assignment

# Basic Assignment (=)
x = 5

# Addition and Assignment (+=)
y = 10
y += 5

# Subtraction and Assignment (-=)
z = 15
z -= 3 

# Multiplication and Assignment (*=)
w = 2
w *= 4 

# Division and Assignment (/=)
q = 20
q /= 5 

# Modulus and Assignment (%=)
r = 17
r %= 3 

# Floor Division and Assignment (//=)
t = 30
t //= 4

# Exponentiation and Assignment (**=)
s = 2
s **= 3

# 5 - BITWISE OPERATORS - used to perform bitwise operations on integers
# work at the binary level, manipulating individual bits of numbers

# AND (&) - performs a bitwise AND operation on corresponding bits of two integers
# If both bits are 1, the result bit is 1; otherwise, it is 0
x = 5  # binary: 0101
y = 3  # binary: 0011
result = x & y # binary result: 0001
print(result) # 1


# OR (|) - performs a bitwise OR operation on corresponding bits of two integers
# If at least one of the bits is 1, the result bit is 1; otherwise, it is 0
x = 5  # binary: 0101
y = 3  # binary: 0011
result = x | y  # binary result: 0111

# XOR (^) - performs a bitwise XOR (exclusive OR) operation on corresponding bits of two integers
# If the bits are different, the result bit is 1; if they are the same, the result bit is 0
x = 5  # binary: 0101
y = 3  # binary: 0011
result = x ^ y  # binary result: 0110

# Complement (~) - performs a bitwise NOT operation, which flips all the bits of an integer
# It returns the two's complement of the integer, which is -(x+1).
x = 5  # binary: 0101
result = ~x  # binary result: 1010

# Left Shift (<<) - shifts the bits of an integer to the left by a specified number of positions
# It effectively multiplies the integer by 2 raised to the power of the shift amount
x = 5  # binary: 0101
result = x << 2  # binary result: 10100 

# Right Shift (>>): - shifts the bits of an integer to the right by a specified number of positions
# It effectively divides the integer by 2 raised to the power of the shift amount (integer division)
x = 10  # binary: 1010
result = x >> 1  # binary result: 0101

# 6 - MEMBERSHIP OPERATOR - used to check if a value is present in a sequence or collection

# in - checks if a value is present in a sequence (such as a list, tuple, string, or set)
#  - returns True if the value is found in the sequence, and False otherwise
numbers = [1,2,3,4,5]
if 3 in numbers:
    print("3 is present in the list.")
else:
    print("3 is not present in the list.")


text = "Hello, World!"
if 'o' in text:
    print("The letter 'o' is present in the string")

# not in - checks if a value is not present in a sequence
#  - returns True if the value is not found in the sequence, and False if it is found
numbers = [1, 2, 3, 4, 5]
if 6 not in numbers:
    print("6 is not present in the list")


text = "Hello, World!"
if 'x' not in text:
    print("The letter 'x' is not present in the string")



# 7 - IDENTITY OPERATOR - used to compare the memory locations of two objects
    
# is - checks if two variables refer to the same object in memory
#  -  returns True if the variables point to the same memory location, and False otherwise
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # False (x and y point to different memory locations)
print(x is z)  # True (x and z point to the same memory location)



a = 5
b = 5

print(a is b)  # True (a and b point to the same memory location for integer 5)

# is not - checks if two variables do not refer to the same object in memory
#  - returns True if the variables do not point to the same memory location, and False if they do
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is not y)  # True (x and y point to different memory locations)
print(x is not z)  # False (x and z point to the same memory location)



a = 5
b = 5

print(a is not b)  # False (a and b point to the same memory location for integer 5)






