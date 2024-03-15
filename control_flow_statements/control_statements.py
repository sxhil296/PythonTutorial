# control flow statements - break, continue, pass, else and exit(). AKA loop control statements


# break - used to terminate the loop, even if the loop condition is true. Transfer the control to the statement immediately after the loop
for i in range(4):
    if i == 3:
        break
    print(i)

while True:
    user_input = input("Enter a number : ")
    if user_input == "exit":
        break
    print(f"Number entered: {user_input}")
print("User entered exit.")

# continue - skips the rest of the code inside a loop for the current iteration and continues with the next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

for letter in "hello":
    if letter == "l":
        continue
    print(letter)

# pass - used to write an empty block of code. it does nothing. used when a statement is required syntactically but you don't want to execute it.
for i in range(5):
    pass

if True:
    pass

# else - executes a block of code when the loop terminates normally
for num in range(1,4):
    print(num)
else:
    print("loop completed normally.")


i = 0
while i < 10:
    print(i)
    i += 1
    if i == 3:
        continue #skips printing 3
    if i == 7:
        break #exits the loop when i reaches 7
else:
    print("Normally")


# exit() - not a standard control flow statement, exit() is used to exit python interpreter
for x in range(10):
    if x == 5:
        exit()
    print(x)

# another syntax of exit()
    # import sys
    # if condition:
    #     sys.exit(1)

