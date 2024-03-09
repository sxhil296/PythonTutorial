# unordered collection of unique elements
# mutable
# {}

my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
print(type({}))

another_set = set()
print(type(another_set))


# add another element
my_set.add(6)
print(my_set)

# remove an element, gives KeyError if absent, returns None
my_set.remove(3)
print(my_set)

# removes an element, doesn't give error
my_set.discard(2)
print(my_set)

# add elements from iterable (such as a list or tuple) 
my_set.update([2,3])
print(my_set)

# sort the set, returns a list, you will have to convert it into a set 
print(set(sorted(my_set)))

# removes and return an arbitrary element, raises KeyError if the set is empty
print(my_set.pop())
print(my_set)

# copy
new_set = my_set.copy()
print(new_set)

# length - Returns the number of elements in the set.
length = len(new_set)
print(length)

# Checks if an element is present in the set
if 3 in my_set:
    print("3 is present.")



# removes all elements from the set
my_set.clear()
print(my_set)


# deletes the set
del my_set



# set operations
set_one = {1,2,3,6,7,'a','b'}
set_two = {1,2,4,5,'a','c'}

# union - Returns a new set containing all unique elements from both sets
# set_union = set_one.union(set_two)
set_union = set_one | set_two
print(set_union)

# intersection - Returns a new set containing only the common elements between two sets.
# set_intersection = set_one.intersection(set_two)
set_intersection = set_one & set_two
print(set_intersection)


# difference - Returns a new set containing elements that are in the first set but not in the second set.
# set_difference = set_one.difference(set_two)
# a-b != b-a
set_difference = set_one - set_two
print(set_difference)


# symmetric difference - Returns a new set containing elements that are in either of the sets, but not both.
set_sym_diff = set_one.symmetric_difference(set_two)
print(set_sym_diff)


# subset
is_subset= set_one.issubset(set_two) # True or False
print(is_subset)

# superset
is_superset= set_one.issuperset(set_two)
print(is_superset)

# disjoint - if no element is common
is_disjoint = set_one.isdisjoint(set_two)
print(is_disjoint)






# difference_update() -  removes all elements from the set that are also present in another specified set. 
# - modifies the set in place and returns None.
# -to update a set by removing elements that are common with another set. 
# - difference() method return a new set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1.difference_update(set2)
print(set1)



# intersection_update() - updates the set with the intersection of itself and another set. 
# - modifies the set in place and returns None.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.intersection_update(set2)
print(set1)

# symmetric_difference_update() - updates the set with the symmetric difference of itself and another set.
#  modifies the set in place and returns None.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.symmetric_difference_update(set2)
print(set1)



# FROZENSET
# - immutable version of a set
# - methods like add(), remove(), and pop() are not available for frozenset objects.
# - can perform operations like intersection, union, difference, and symmetric difference, return new frozenset objects rather than modifying the original object
# - useful in situations where you want to use a set as an element of another set, or as a key in a dictionary.


sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
frozen_sets = [frozenset(s) for s in sets_list]

common_elements = frozen_sets[0].intersection(*frozen_sets[1:])
print(common_elements)

set1 = frozenset({1, 2, 3, 4})
set2 = frozenset({3, 4, 5, 6})

intersection = set1.intersection(set2)
print(intersection)  # Output: frozenset({3, 4})

union = set1.union(set2)
print(union)  # Output: frozenset({1, 2, 3, 4, 5, 6})

difference = set1.difference(set2)
print(difference)  # Output: frozenset({1, 2})

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output: frozenset({1, 2, 5, 6})
