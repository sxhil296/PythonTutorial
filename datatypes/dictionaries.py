# ordered collection of items (previously unordered)
# items can be of any data type
# stores data in key:value pair
# not indexed like lists or tuples.
# {}

my_dict = {"one": 1, "two": 2,  "three": 3}
print(my_dict)
print(type(my_dict))
print(type({}))

print(my_dict["one"])


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