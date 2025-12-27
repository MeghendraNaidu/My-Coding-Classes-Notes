# 1. Single Inheritance
class Vehicle:
    compant_name = "TATA"
    
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        print("Vehicle constructor called")
    
    def Drive(self):
        print("Vehicle in Deive Mode")

class Car(Vehicle):
    
    def __init__(self, vehicle_id, vehicle_type):
        super().__init__(vehicle_id, vehicle_type)
        self.model_num = 1234
        # print(self.model_num)
        print("Car constructor called")
    
    def Drive(self):
        super().Drive()
        print("Car in Deive Mode")
    
    def describe(self):
        print(self.vehicle_id, self.vehicle_type, self.model_num)

# class Bike(Vehicle):
#     pass

# class ElectricCar(Car):
    
#     # def Drive(self):
#     #     print("")
#     pass

c1 = Car(23, "road transport")
# b1 = Bike()
# v1 = Vehicle()
# e1 = ElectricCar()

c1.Drive()
c1.describe()
# b1.Drive()
# v1.Drive()


# Multiple Inheritance

class Lion:
    
    def roar(self):
        print("Balayya is roaring")

class Tiger:
    
    def hunt(self):
        print("NTR is hunting")
        
    def roar(self):
        print("NTR is roaring")

class Liger(Lion, Tiger): # MRO = Method Resolution Order
    pass

# MRO = Method Resolution Order


lg1 = Liger()

lg1.roar()
# lg1.hunt()

print(Liger.mro())
print(Liger.__mro__)
