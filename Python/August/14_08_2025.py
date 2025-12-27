# Functions => Functions is a block of code which can executed when ever we call it.
# Functions => Scope
# Types of Scopes 
# 1. Global Scope = G
# 2. Local Scope = L
# 3. Enclosed Scope = E
# 4. Built In Scope = B
#Order is "LEGB"


# Global Scope => The Variables can access any where in the file
num1 = 10
# print(num1)
# if 3 > 2:
#     print(num1)
    
# for i in range(1, 10):
#     print(num1)
    
# def check_scope():
#     print(num1)
    
# check_scope()

# Local Scope => The Variables can access only inside the function and we cannot access it outside.

num1 = 32  # It is Global Scope
def check_function(): # when we declare a function it becomes global scope
    num2 = 10  # Local Scope
    print(num2)
    print(num1)
    def nested_function():
        print("Output from nested function") # after declaration it is local scope we can access only inside the function
    nested_function() # we can only use inside the outer function and we cannot use outside the outerr function

check_function()
# print(num1)
# print(num2)

# Enclosed Scope

def first_function():
    temp = "Good Morning"
    
    def second_function():
        print(temp)
    second_function()
    print(temp)
    
# Built In Scope
print(len("Hi"))



num1 = 25

def test_function():
    num1 = 40
    print(num1)

test_function()
print(num1)


temp = "Good Afternoon"
def first_function():
    temp = "Good Morning"
    
    def second_function():
        temp = "Good Evening"
        print(temp)
        
    second_function()
    print(temp)
    
first_function()

num5 = 32
num4 = 65

def check_function():
    num4 = 77
    # print(num5)
    def inner_function():
        num4 = 88
        print(num4)
    inner_function()
    print(num4)

check_function()
print(num4)