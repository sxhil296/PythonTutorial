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