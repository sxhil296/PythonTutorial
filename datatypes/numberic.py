# Numeric data types holds numerical values. Types - integer, float and complex

# Numbers are immutable in Python


int_number = 4
print(f"Integer number : {int_number}")

float_number = 4.2
print(f"Float number : {float_number}")

complex_number=2+3j
print(f"Complex number : {complex_number}")


num1 = 10
num2 = 5
sum_result=num1+num2
difference_result=num1-num2
product_result=num1*num2
exponent_result=num1**3
remainder_result=num1%3
division_result=num1/3
floor_division= num1//3
is_equal = num1==num2
print(abs(-10))
print(max(2,3,5))
print(min(2,4,5))


# binary literals - base 2 - starts with 0b or 0B
bin_num = 0b1111
print(bin_num)
print(bin(15))

# octal literals - base 8 numbers - starts with 0o or 0O
#  0o12 - 1*8+2*1 = 10
octal_value = 0o12
print(octal_value)
print(oct(10))

# hexadecimal literals - base 16 - starts with 0X or 0x
# 0x14 - 1*16+1*4 = 20
hex_value = 0x14
print(hex_value)
print(hex(20))


# random module
import random

print(random.random()) #[0.0,1.0)
print(random.randint(1,10)) #[1,10]
print(random.uniform(1,10)) #[1.00, 10.00]

list_one=[1,2,3,4,5,6]
print(random.choice(list_one))
random.shuffle(list_one)
print(list_one)




