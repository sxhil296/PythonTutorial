#DATA TYPES IN PYTHON
# Few built-in data types in python are:

# Numbers
a = 5
print("The type of a is:",type(a))                                  #type of variable
b = 40.5
print("The type of b is:",type(b))                                  #type of variable
print("b is a floating point number",isinstance(40.5,float))
c = 1+3j
print("The type of c is:",type(c))                                  #type of variable
print("c is a complex number",isinstance(1+3j,complex))             

#string
str1 = "hello python"
str2 = "how are you"
print(str1[0:2])
print(str1[4])
print(str1*2)
print(str1 +str2)

#list
li1 = [1,"hi","python",2]
print(type(li1))                                                      #type of list
print(li1)                                                            #print the list
print(li1[3:])                                                        #list slicing
print(li1[0:2])                                                       #list slicing
print(li1 + li1)                                                      #list concatination
print(li1*2)                                                          #list repetition

#tuple
tu1 = (20 , "apple","sky",12.4)                                       #define a tuple
print(type(tu1))                                                      #type of tuple
print(tu1)                                                            #print the tuple
print(tu1[0:3])                                                       #slicing a tuple
print(tu1[:2])                                                        #slicing a tuple
print(tu1 + tu1)                                                      #concatination of tuple
print(tu1 * 3)                                                        #repition of tuple
tu1[3] = 30                                                           #adding a new element in a tuple results in error


#dictionary
d = {1:'Aakash', 2:'Suman', 3:'Janvi', 4:'Ravi'}                      #define a dictionary
print(d)                                                              #print a dictionary
print("1st name is",d[1])                                             #accessing a dictionary
print("2nd name is"+d[4])
print(d.keys())                                                       #accessing keys 
print(d.values())                                                     #accessing values


#boolean
print(type(True))                                                     #class boolean
print(type(False))
a = False                                                             #define a boolean
print(a is True)                                                      #print bool is true

#set
set1=set()                                                            #creating empty set
set2={20, 'python', 82.3, 'Alex'}                                     #creating a set
print(set2)                                                           #printing a set 
set2.add(30)                                                          #adding an element in the set
print(set2)                                                           #accesing modified set
set2.remove(30)                                                       #removing an element from the set
print(set2)
print(set1)
