class Car():

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    # polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"

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

    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85KWH")

third_car = Car("Tata", "Safari")
print(my_tesla.get_brand())
my_tesla.set_brand("Tessslaa")
# print(my_tesla.brand)
print(my_tesla.get_brand())
print(my_tesla.fullname())
print(my_tesla.fuel_type())


print(third_car.fuel_type())
print(Car.total_car)








