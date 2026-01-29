class Car:
    def __init__(self,brand,year):
        self.__brand=brand # using __ is making it private.
        self.__year=year
    def get_brand(self): # Encapsulation.
        return self.__brand +"!!!"
    def fullname(self):
        return f"{self.__brand}{self.__year}"
    @staticmethod
    def staticmethod():
        return "cars are means of transport"
    @property
    def year(self):
        return self.__year

    
class ElectricCar(Car): #Inheritence
    def __init__(self,brand,year,battery_size):
        super().__init__(brand,year)
        self.battery_size=battery_size


    
electric_car=ElectricCar("Tesla","2023","86kWh")

print(electric_car.fullname())
print(electric_car.battery_size)
print(electric_car.__brand) #AttributeError: 'ElectricCar' object has no attribute '__brand'
print(electric_car.get_brand())

car_obj=Car("Mahindra","2020")
print(Car.staticmethod()) #this gives output
print(car_obj.staticmethod()) #this will not be able to get access by objects so to do so add @staticmethod before function decleration
print(car_obj.brand,car_obj.year)
print(car_obj.fullname())
car_obj.year="2025" # it can be writable so to prevent that we use property decorators
print(car_obj.year())

print(isinstance(electric_car,Car)) #true
print(isinstance(electric_car,ElectricCar)) #true
print(isinstance(car_obj,Car)) #true
print(isinstance(car_obj,ElectricCar))# false

#Multiple Inheritence

class Batery():
     def batery_info(self):
      return "This is battery info"
class Engine():
    def engine_info(self):
        return "this is battery info"
class Tesla(Batery,Engine,Car):
    pass
new_tesla=Tesla("Tesla","2027")
print(new_tesla.batery_info())
print(new_tesla.engine_info())