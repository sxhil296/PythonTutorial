class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def fullname(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
second_car = Car("Mahindra", "Scorpio")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())
# print(second_car.fullname())

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.brand)
print(my_tesla.get_brand())
# print(my_tesla.fullname())



# encapsulation





# __init__ is a constructor 
# class Greet():
#     def __init__(self, name, greeting):
#         self.name = name
#         self.greeting = greeting

#     def sayGreetings(self):
#         return f"{self.greeting}, {self.name}! How are you today?"

# greeter = Greet("John Doe", "Hello")
# print(greeter.sayGreetings())

# sahil_greeter = Greet("Sahil", "Salam")
# print(sahil_greeter.sayGreetings())