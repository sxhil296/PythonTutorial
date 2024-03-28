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

def greeting():
    print("Hello, World!")

greeting()

def greet(name):
    return f"Hello, {name}!"

result = greet("Sahil")
print(result)




