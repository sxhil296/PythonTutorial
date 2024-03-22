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