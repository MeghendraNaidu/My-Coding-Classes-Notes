# Polymorphism = # 1. Method Overloading, 2. Method Overriding, 3. Operator Overloading

#Method Overloading => 

# def add(a, b):
#     return a + b

# def add(a, b, c):
#     return a + b + c

def add(*a):
    return sum(a)

add(2, 3)
add(2, 3, 4)

# Method Overriding = 

class Human():
    def talk(self):
        print("Human is Talking")

class Student(Human):
    def talk(self):
        print("Student is talking with his knowledge")
        
# why is it included in Polymorphism ?

# Operator Overloading = 
2 + 3
'2' + '3'
[1, 2] + [3, 4, 5]