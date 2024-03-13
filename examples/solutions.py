# 1 - Print Hello world!
print("Hello, World!")

# 2 - Add Two Numbers
num1 = 5
num2 = 6
result = num1 + num2
print(result)

# 3 - Add Two Numbers With User Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"Sum : {result}")

# 4 - Find the Largest Among Three Numbers
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3 ):
    largest_number= num1
elif (num2 >= num3) and (num2 >= num1):
    largest_number = num2
else:
    largest_number = num3
print(f"Largest number among {num1}, {num2} and {num3} is {largest_number}.")


# 5 - Find the largest item in an iterable
numbers = [9, 34, 11, -4, 27]
largest = max(numbers)
print(largest)

# 6 - Find square root
square = 64
square_root = square ** 0.5
print(f"Square root of {square} is {square_root}.")

# 7 - Find square root of real or complex numbers
import cmath

num = 1+2j
num_sqrt = cmath.sqrt(num)
print(f"{num_sqrt:.3f}")

# 8 - Calculate the area of a triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

s = (a+b+c)/2
area_of_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"Area of the given triangle is {area_of_triangle:.2f}")

# 9 - Check Prime Number
num = 8

if num > 1:
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(f"{num} is a prime number.")
    else:
         print(f"{num} is not a prime number.")
else:
     print(f"{num} is not a prime number.")


# 10 - Find the Factorial of a Number
number = int(input("Enter a number to find factorial: "))
factorial = 1
if number < 0:
    print("Please enter a positive number.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(f"Factorial of {number} is {factorial}.")




