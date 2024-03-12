# strings are sequence of characters enclosed within ' ' or " " or """ """
# strings are also immutable

str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = """This is a 
multiline string."""
print(str1)
print(str2)
print(str3)


print(str1[0])
print(str1[-1])
print(str1[1:4])
length = len(str1)
uppercase = str1.upper()
lowercase = str1.lower()
capitalize = str1.capitalize()
title_case = str1.title()
concatenated_str=str1+" "+str2
repeated_str = str1*3

names = "Emir, Levi, Eren"
print(names)
print(type(names))
new_names = names.replace("Eren", "Malik")
print(new_names)
print(names) #this shows that strings are immutable cause changes didn't occur in the original string but a new copy was formed i.e. new_names
position = names.find('Levi')  #doesn't give error if absent
index = names.index("Jay") #raises error if absent i.e. valueError


names_list = names.split(', ')
print(names_list)

name_str = ', '.join(names_list)
print(name_str)

example = "pythonnn"
print(example.count('n'))
print(example.startswith('s'))
print(example.endswith('n'))


escaped_str1="Emir's Laptop"
escaped_str2='Emir\'s Laptop'
raw_str=r'Emir\n Laptop'

str_one = "hello"
reversed_str_one = str_one[::-1]
print(reversed_str_one)






