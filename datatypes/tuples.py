#ordered collection
#immutable
#can store diff data types
#useful when we want data to remain unchanged
# duplicity is allowed

my_tuple = (0,1,2,3,4,5)
my_tuple2 = ('a','b','c','d','e')
my_tuple_without_brackets = 0,1,2,3,4,5
print(my_tuple)
print(my_tuple_without_brackets)
print(type(my_tuple))
print(type(my_tuple_without_brackets))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:])
print(my_tuple[0:3])
print(my_tuple[:4])
print(my_tuple[:])
print(my_tuple[-1])
print(my_tuple[::-1])

# can't change values, the following example will give an error i.e typeError
# my_tuple[0] = 10

# len() method returns the number of elements
length = len(my_tuple)

concatenated_tuple = my_tuple+my_tuple2
print(concatenated_tuple)


repeated_tuple = my_tuple2*4


random_tuple = (5,4,2,6,7,8)
print(sorted(random_tuple)) #returns a sorted list
print(tuple(sorted(random_tuple))) #will return a sorted tuple

occurrence = my_tuple.count(2)
find_index = my_tuple.index(3)

del my_tuple
# print(my_tuple) will raise NameError

# empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))




