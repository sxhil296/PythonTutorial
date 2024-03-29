# functions are block of code that perform a specific task
# allows to break down code into smaller modular pieces
# promote code reusability (through function call)

# function definition - 'def' keyword is used followed by function's name and () containing parameters
# if no parameter needed, we use ()
# function call - function_name(arguments) - calls the function to perform the action


# parameters - variables or placeholders in () in function definition
# arguments - values passed into the function when it is called

''' In the context of programming:

- A **function** is a block of code that is organized and named, designed to perform a specific task. Functions are independent and can be called from anywhere in the code. In Python, functions are defined using the `def` keyword.

- A **method** is a function that is associated with an object. Methods are called on objects and operate on the data within the object. In object-oriented programming, methods are functions defined within a class and are accessed using an instance of that class.

Here is a simple example in Python to illustrate the difference:

```python
# Function example
def greet():
    print("Hello!")

# Method example
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Using the function
greet()

# Using the method
person = Person("Alice")
person.greet()
```

In this example:
- `greet()` is a function that can be called directly.
- `greet()` inside the `Person` class is a method that operates on the `Person` object.

Functions are standalone blocks of code, while methods are functions associated with objects in object-oriented programming.'''


# a basic function syntax
def greeting():
    print("Hello, World!")

greeting()

#? NOTE : avoid using 'print()' inside function definition (for flexibility, testing and debugging, reusability of code, etc), use 'return' instead

# a function with a parameter
def greet(name):
    return f"Hello, {name}!"

result = greet("Sahil")
print(result)



# a function to calculate the square of a number
def find_square(number):
    return number**2

result = find_square(5)
print(result)



# a function to calculate the square of a number with user input
def find_square_user_input():
    num = int(input("Enter a number: "))
    return num**2

answer = find_square_user_input()
print(f"The square of your number is {answer}")




# function with multiple parameters
def find_sum(a, b):
    return a * b

print(find_sum(3, 4))




# polymorphism(cheez ek, kaam anek) in functions
# function which multiply two numbers and strings as well
def multiply(p1, p2):
    return p1 * p2

print(multiply(3, 4))
print(multiply('a', 7))
print(multiply(7, 'h'))



# function returning multiple values
# area and circumference of a circle given its radius
import math
def area_and_circumference(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

# print(area_and_circumference(7))
a, c = area_and_circumference(7)
print(f"Area : {a:.2f}")
print(f"Circumference : {c:.2f}")



# function with default parameter
def say_hello(name="World"):
    return f"Hello, {name}!"

print(say_hello("John"))
print(say_hello())


# lambda function or anonymous function - functions without name - often used when you need a simple function for a short period and don't want to define a full function using the def keyword
cube = lambda x: x ** 3
print(cube(3))

# lambda function to calculate the square of the sum of two numbers a and b
square_sum = lambda a, b:(a + b) ** 2
print(square_sum(5, 6))


# function with *args (variable number of arguments)
# '*' indicates that the number of args is variable 
# use '*args" for better code readability
# def sum_all(*args):
#     return sum(args)
def sum_all(*nums):
    print(*nums)
    # print(type(*nums)) gives error
    print(nums)
    print(type(nums)) #tuple
    return sum(nums)

print(f"Sum : {sum_all(1,2,3)}")


def  multiply_numbers(*args):
    for i in args:
        print(i*2)
    
multiply_numbers(1,2,3)


# function with **kwargs (keyword arguments)
# often used in situations where you need to pass multiple optional arguments to a function and you want to pass them in the form of key-value pairs.

def print_details(**kwargs):
    print(kwargs)
    print(type(kwargs)) #dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=30, city="New York")
print_details(name="Shaktiman", power="Lasers", city="Mumbai")



# function with yield
# useful for scenarios where you need to generate a sequence of values without storing them all in memory at once
# a generator function that yields even numbers upto a limit

def generate_even_numbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            # return i
            # print(i)
            yield i

gen = generate_even_numbers(9)
for x in gen:
    print(x)


'''
return: Think of return as a function that gives you a single result and then says, "I'm done." Once it gives you the result, it doesn't do anything else.

yield: On the other hand, yield is like a function that can give you multiple results one after the other. It pauses after each result and says, "I'll give you more when you ask for it." It remembers where it paused so it can continue from there later.
'''


# recursive function - a function which calls itself from within
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

