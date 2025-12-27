# Abstraction = means hiding
# Hiding implementation detailes of methods

# Abstract Method
# Abstract Class => you cannot create an object for abstract class


from abc import ABC, abstractmethod


class AbstractExample(ABC):
    
    @abstractmethod
    def show_details(self):
        pass
    def example_check(self):
        print("This is an example")
        
class ATM(ABC):
    
    @abstractmethod
    def show_details(self):
        pass
    def example_check(self):
        print("This is an example")
        
class SBI_ATM(ATM):
    
    def show_details(self):
        print("SBI implementation details")

class ICICI_ATM(ATM):
    
    def show_details(self):
        print("ICICI implementation details")
        
# abc1 = AbstractExample()


class Vehicle:
    def __init__(self):
        print("Vehicle Constructor called")
        
    def __del__(self):
        print("Logging in progress")
        print("Vehicle abject deleted")

vh1 = Vehicle()
vh2 = Vehicle()
vh3 = Vehicle()
vh4 = Vehicle()
vh5 = Vehicle()

del vh1

for i in range(1, 20):
    print("Hi")