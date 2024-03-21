# the process of converting one data type into another
# aka as type casting
# implicit(automatic) type conversion and explicit(manual) type conversion
# no loss of data in implicit
# loss of data in explicit
# implicit is preferable



# EXPLICIT TYPE CONVERSION EXAMPLES

# int(x): Converts x to an integer. If x is a float, it will be truncated towards zero
x = 5.6
y = int(x)
print(y)
print(type(y))


# float(x): Converts x to a floating-point number.
x = 6
y = float(x)
print(y)
print(type(y))


# str(x): Converts x to a string.
x = 5
y = str(x)
print(y)


# bool(x): Converts x to a Boolean value. Returns False for 0, None, empty sequences, and empty mappings; otherwise, returns True.
x = 0
y = bool(x)
print(y) 


# list(x): Converts x to a list. x can be any iterable (e.g., tuple, string, set).
x = (1, 2, 3)
y = list(x)
print(y)


# tuple(x): Converts x to a tuple. x can be any iterable (e.g., list, string, set).
x = [1, 2, 3]
y = tuple(x)
print(y) 



# IMPLICIT TYPE CONVERSION

'''Implicit type conversion, also known as automatic type conversion, occurs when the interpreter automatically converts one data type to another without any explicit instruction from the user. This typically happens when you perform operations between different data types.'''

x = 5  # integer
y = 2.5  # float
z = x + y  # adding an integer and a float

print(z)  # Output: 7.5
print(type(z))  # Output: <class 'float'>
