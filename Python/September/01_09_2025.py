# OOPS Concepts

# Procedural Code Disadvantages = means without oops
# 1. Code Maintainability
# 2. Data Security, Code Exposure
# 3. Code reuse

# Class and Object

# Object = Real World Entity
# Behaviour and Data
# Methds and Variables

class Calculator:
    id = 45
    manf_date = '01-sep'
    def add(self, a, b):
        print(a + b)
        print(self.id)
        
    def sub(self, a, b):
        print(a - b)
        
    def mul():
        print("Hello")
        
    def describe(self): # self is not mandatory variable we can write any variable but it should be in first place
        print(self.id, self.manf_date)
        

clc1 = Calculator()
clc2 = Calculator()
clc3 = Calculator()
clc4 = Calculator()

clc1.add(2, 3)
# clc2.add(4, 5)
# clc2.add(9, 11)
# cl.mul()

# Adding Variables => 
# There are 2 Ways => 1. Manual Way  2. Using Constructors

# 1. Adding Variables using Manual Way
# clc1.id = 45
# clc1.manf_date = "01-Sept"
# clc2.manf_date = "02-Sept"

# print(clc1.id)
# print(clc1.manf_date)
# print(clc2.manf_date)

clc1.describe()
# clc3.describe()