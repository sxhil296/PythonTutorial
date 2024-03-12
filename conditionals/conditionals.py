# conditional statements are used to control the flow of the program based on certain conditions
# if, elif, else, nested if

# if - used to execute a block of code if a condition if true
x = 10
if x <= 10:
    print("x is smaller than or equal to 10.")

# if...else - used to execute one block of code if the condition is true, and another block of code if the condition is false.
a = 10
if (a % 2 == 0):
    print("a is even")
else:
    print("a is odd")

# if...elif...else -  used to check multiple conditions. It executes the first block of code whose condition is true, and skips the rest.
y = 0
if y > 0:
    print("y is positive.")
elif y < 0:
    print("y is negative.")
else:
    print('y is zero.')

# nested if - if statements within other if, elif or else block to check more complex conditions
z = 10
if z > 0:
    if z % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is not a positive number")

# ternary - shorthand notation of if-else

score = 56
# result = "A" if score >= 85 else "B" if score >= 70 else "C" if score >= 55 else "D"
result = "A" if score >= 85 else "B"

print(result)