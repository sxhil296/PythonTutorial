## keywords
- pre defined reserved words that have special meanings to the compiler
- all keywords are in lowercase except True, False and None
- keywords can't be used as variable or function or identifier name

## identifier
- name given to variable, class, methods, etc
- can't be a keyword
- case sensitive
- always start with a letter or _
- no special character or whitespace
- doesn't start with a number
  
## variable
- container (storage area) to hold data
  ```
  number = 10
  <!-- here 'number' is a variable holding the value '10' -->

  a, b, c = 1, 2.5, "Hello"
  ```

## constants
- variables whose value can't be changed
- usually declared and assigned in a module
- capital letters is a convention for constants

## literals
- representative of a fixed value in a program

## statement
- a statement is a unit of code that the Python interpreter can execute. OR
- a statement is a single instruction that the Python interpreter can execute
- it typically performs some action or operation
```
# Assignment statement
x = 10

# Conditional statement
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Loop statement
for i in range(5):
    print(i)

# Import statement
import math

# Function definition statement
def greet(name):
    print("Hello, " + name)

greet("Alice")
```