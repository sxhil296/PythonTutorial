# ordered collection of items (previously unordered, before python 3.7)
# the order in which key-value pairs are inserted into a dict is preserved when iterating
# can't have same keys
# items can be of any data type
# stores data in key:value pair
# not indexed like lists or tuples.
# {}
# mutable

my_dict = {"one": 1, "two": 2,  "three": 3}
print(my_dict)
print(type(my_dict))
print(type({}))

print(my_dict["one"]) #gives error if absent"


key_list = my_dict.keys()
print(key_list)
print(type(key_list))
#key_list is not a true list, so cannot use index methods, TypeError
list_of_keys = list(key_list)
print(list_of_keys[0])

value_list = my_dict.values()
print(value_list)
print(type(value_list))
#value_list is not a true list, so cannot use index methods, TypeError
val_list = list(value_list)
print(val_list[0])

items_list = my_dict.items()
print(items_list)
#items_list is not a true list, so cannot use index methods, TypeError
item = list(items_list)[0]
print(item)


# prints the value of the specified key, doesn't give error if absent
print(my_dict.get("one"))

user = {"name": "Levi", "age":23, "male": True}
print(user)

# change value
user["age"] = 24
print(user)

# add new key:value pair i.e element
user["city"] = "NY"
print(user)

# add new item
user.update(country = "Japan")
print(user)

# update existing item, adds the new element if the key specified is not present
user.update({"country": "Walls"})
print(user)


# length of the dictionary
print(len(user))

# pop removes the element specified by the key and returns its value, gives error if absent KeyError
print(user.pop("city"))
print(user)

# popitem removes the arbitrary element and returns its value
print(user.popitem())
print(user)

# del method removes a specified element, returns None, gives error KeyError if absent
del user["age"]
print(user)

# deletes the entire dictionary
# del user 

# empty the dictionary
user.clear()
print(user)


# dictionary from lists (both lists should have same number of elements, longer one will be truncated and keys must be unique)
key = ['a', 'b', 'c', 'd']
value = [1, 2, 3, 4]
new_dict = dict(zip(key, value))
print(new_dict)


default_value = "default"
new_dict_two = dict.fromkeys(key, default_value)
print(new_dict_two)


# dict comprehension - a concise and efficient way to create dictionaries in a single line of code
# Syntax: {key_expression: value_expression for item in iterable if condition}
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
person_info = {key: value for key, value in person.items() if key != 'city'}
print(person_info)

squares = {x:x**2 for x in range(10) if x%2==0}
print(squares)


keys = ['one', 'two', 'three']
values = [1, 2, 3]
comp_dict = {k:v for k, v in zip(keys,values)}
print(comp_dict)

# Creating a nested dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grades": {
        "math": 90,
        "science": 85,
        "history": 88
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "123-456-7890"
    }
}

# Accessing values in the nested dictionary
print("Student Name:", student["name"])
print("Math Grade:", student["grades"]["math"])
print("Email:", student["contact"]["email"])