# getter methods
# used to retrieve the values of private attributes (in encapsulation.)
# aka as accessor methods because they allow access to the attributes' values without directly exposing the attributes themselves
# names prefixes with 'get' followed by the attribute name



# setter methods are used to modify the values of private attributes
# aka as mutator methods because they allow modification of the attributes' values in a controlled manner
# names prefixed with 'set' followed by the attribute name.


class Person:
    def __init__(self, name, age):
        self.__name = name #private attribute
        self.age = age

    def get_name(self): #getter method
        return self.__name
    
    def set_name(self, new_name): #setter method
        self.__name = new_name

person1 = Person("Emir", 20)

# access the private attribute using the getter method
print(person1.get_name())


# modify the private attribute using the setter method
person1.set_name("Mallick")

print(person1.get_name())

