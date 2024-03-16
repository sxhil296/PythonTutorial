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


# 11 - Swap Two Variables
x = 5
y = 10

print(f"Before swapping : {x}, {y}")
x, y = y, x
print(f"After swapping : {x}, {y}")


# 12 - Convert all the characters of a string to their opposite letter case( uppercase to lowercase and vice versa)
str1 = "EmiR mAliK"
print(str1.swapcase())

# 13 - Generate a random number between 0 and 9
import random
print(random.randint(0, 9))

# 14 - Convert Kilometers to Miles
km = float(input("Enter distance in kilometers: "))
mile = km * 0.621371
print(f"Distance in miles is {mile}")

# 15 - Convert km/h to m/s
speed_kmh = float(input("Enter speed in km/h: "))
speed_ms = speed_kmh / 3.6
print(f"Speed in m/s is {speed_ms}")

# 16 - Convert m/s to km/h
speed_ms = float(input("Enter speed in m/s: "))
speed_kmh = speed_ms * 3.6
print(f"Speed in km/h is {speed_kmh}")

# 17 - Convert Celsius To Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is {fahrenheit}")

# 18 - Convert Fahrenheit To Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Temperature in Celsius is {celsius}")

# 19 - Check if a Number is Positive, Negative or 0
try:
    number = float(input("Enter a number to check: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# 20 - Print all Prime Numbers in an Interval
for x in range(1,21):
    if x > 1:
        for i in range(2, x):
            if (x % i )== 0:
                break
        else:
            print(x)

# 21 -  Check if a Number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# 22 - Palindrome checker
user_string = input("Enter a string: ")
if user_string == user_string[::-1]:
    print(f"{user_string} is a palindrome")
else:
    print(f"{user_string} is not a palindrome.")

# 23 - Display a the multiplication of a number
table_number = int(input("Enter a number to print the table: "))
for num in range(1,11):
    print(f"{table_number} X {num} = {table_number*num}")

# 24 - Check Armstrong Number
# abcd... = an + bn + cn + dn + ...
# 153 = 1*1*1 + 5*5*5 + 3*3*3 
try:
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    if num < 0:
        print("Please enter a positive number.")
    else:
        num_digits = len(str(num))

        sum_of_cubes = sum(int(digit) ** num_digits for digit in str(num))

        if num == sum_of_cubes:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# 25 - Calculate the sum of numbers in the list
numbers = [1,2,3,4,5,6]
result = sum(numbers)
print(f"Sum of the numbers in the list: {result}")

# 26 - Find sum of n natural numbers
num = int(input("Enter the natural number:"))
result_of_sum = 0
for x in range(0, num+1):
    result_of_sum += x
print(result_of_sum)

# 27 - Display Powers of 2
try:
    num_terms = int(input("Enter the number of terms for powers of 2: "))
    if num_terms <= 0:
        print("Please enter a positive number.")
    else:
        for x in range(num_terms+1):
            result = 2 ** x
            print(f"2^{x}={result}")
except ValueError:
    print("Please enter a valid integer.")