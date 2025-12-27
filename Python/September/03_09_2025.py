# Decorators adds additional Functionality to Exisiting Functions. Decorators are also functions

def example_decoretor(func):
    def wrapper():
        print("Check Requirements like paper, ink")
        func()
        print("Thank You")
    return wrapper


@example_decoretor
def printer():
    print("Printing in progress")

printer()

# @example_decoretor
# def fax():
#     print("fax in progress")

# fax()

# 4 Pillers = A, P, I, E

# Inheritance = Why?

class Clac:
    def add(self, a, b):
        print(a + b)

class AdvaClac(Clac):
    pass

adv1 = AdvaClac()
adv1.add()

# Types of Inheritance
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchial Inheritance
# 5. Hybrid Inheritance