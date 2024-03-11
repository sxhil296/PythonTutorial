# used to repeat a block of code multiple times
# two types in python - for loop and while loop


# FOR LOOP
# used to iterate over a sequence (like a list, tuple, string, or range) and execute the same code for each item in the sequence.


# iterating over a Range
for x in range(0,10,2):
    print(x)


print("\n")
# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



print("\n")
# iterating over a range and appending a list
nums = []
for x in range(1,20):
    if x % 2 == 0:
        nums.append(x)
print(nums)



print("\n")
# iterating over a string
for char in "hello":
    print(char)


print("\n")
# iterating over a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])


print("\n")
# using Enumerate for Index and Value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# WHILE LOOP
# used to repeatedly execute a block of code as long as a specified condition is true
# useful when you want to iterate based on a condition rather than a sequence

print("\n")
# Iterating Until a Condition is Met
i = 1
while i<=5:
    print(i)
    i += 1



print("\n")
# User Input Validation
while True:
    age = input("Enter the age: ")
    if age.isdigit():
        break
    else:
        print("Invalid input. Please enter a number.")
print("Your age is: ", age)




print("\n")
# Processing Data Until Exhausted
data = [1, 2, 3, 4, 5]
while data:
    print(data.pop())



# ? NOTE: if you know the number of iterations or have a specific sequence to iterate over, use a for loop. If you need to repeat a block of code based on a condition and the number of iterations is not known in advance, use a while loop.