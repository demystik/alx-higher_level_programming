#!/usr/bin/python3
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


# mine = Car("toyota", 'acura', 2002)
# mine.increment_odometer(4)
# print(mine.odometer_reading)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def my_color(self, color):
        self.color = color
    
my_tesla = ElectricCar('Tesla', 'model s', 2018)
# print(my_tesla.get_descriptive_name())
my_tesla.my_color("Silver")
my_tesla.increment_odometer(55)
# print(my_tesla.color)
# print(my_tesla.odometer_reading)

# class Base():
#     istances = 0

#     def __init__(self) -> None:
#         Base.istances += 1
#         self.id = Base.istances
# b = Base()
# print(b.id)


class Base():
    """ My base class """

    instances = 0

    def __init__(self):
        self.instances += 1
        self.id = Base.instances


for i in range(3):
    b = Base()
    print(dir(b))
    # print(b.id)
    # print(b.instances)
