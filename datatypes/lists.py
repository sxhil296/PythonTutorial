# ordered collection of items
# items can be of any data type
# mutable
# []

my_list = [1,2,3,'a','b',True]
print(my_list)
print(type(my_list))

# accessing elements
my_list[0]
my_list[1:4]
my_list[-1]

# modify
my_list.append('c') #adds item in the end
print(my_list)

my_list.insert(3, 'x')  #inserts at specific index
print(my_list)

my_list[0] = 10 #change the value of existing element
print(my_list)

del my_list[0] # deletes the item of index 0
print(my_list)

my_list.remove('b') # removes first occurrence of a given value, raises the error if absent
print(my_list)

print(my_list.pop() ) #removes and returns last item
print(my_list.pop(1))    #removes and returns item with specified index


# concatenation of lists
my_list_two = ["apple", "banana"]
combined_list = my_list+my_list_two
print(combined_list)

# index of an item in the list, raises valueError if item is absent
index = my_list_two.index("apple")
print(f"Index of apple is {index}.")


# length of the list(number of items in the list)
length = len(my_list) 
print(length)

# check if an item exists in the list
fruit = "mango"
if fruit in my_list_two:
    print("Mango is in the list.")
else:
    print("Mango is not in the list.")


# complete deletion
data = [1,2,3,4]
del data
# print(data) # will give NameError

# empty the list and returns an empty list
data_list = [1, 2, 3, 4, 5, 5]
data_list.clear()  
print(data_list)

# find occurrence
data_list_two = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 5]
occurrence = data_list_two.count(5)
print(occurrence)

# sorting a list
numbers = [5, 2, 8]
numbers.sort() #returns none,modifies the original list, applies only on lists
print(numbers)

numbers_list = [2,3,64,7,6]  #on any iterable, returns a new list
print(sorted(numbers_list))

#reverse a list
letters = ['a', 'b', 'c', 'd']
letters.reverse() #doesn't return anything, modifies the original list
print(letters)

# copy
new_list = letters.copy()
print(new_list)

# remove duplicate items from a list
unique_list = list(set(data_list_two))
print(unique_list)
 
#  or 
unique_list_two = []
for item in data_list_two:
    if item not in unique_list_two:
        unique_list_two.append(item)
print(unique_list_two)

# create a list from a string
my_string = "hello"
list_from_string = list(my_string)
print(list_from_string)

list_from_string_two = my_string.split()
print(list_from_string_two)

# list comprehension - a concise and efficient way to create lists in a single line of code
# Syntax: [expression for item in iterable if condition]
nums = [1,2,3,4,5,6,7,8]
squares = [item**2 for item in nums]
print(squares)

evens = [item for item in nums if item%2==0]
print(evens)

