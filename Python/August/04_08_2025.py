# Types of Arguments in Python Functions
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Arbitrary Arguments

# Disadvantages Of Positional Arguments
# 1. Here we need to follow the order of parameters
# 2. If we have more than 3 parameters then it is difficult to remember the order of parameters
# 3. If we want to change the value of a parameter then we need to remember the order of parameters

# Default Arguments
# We do not write the default arguments before non-default arguments. 
# And Default arguments should be in last place and non-default should be in first place.

# In Python Method Overloading is not possible. Because
# def add(a , b):
#     print(a + b)

# def add(a, b, c):
#     print(a + b + c)

# def add(a, b, c, d):
#     print(a + b + c + d)
    
# add(2, 3)
# add(2, 3, 4)
# add(2, 3, 4, 5)
# And we cannot write the same function name with different parameters. Instead we can use Arbitrary Arguments.
# Here Arbitrary Arguments can start with "*" and it can take any number of arguments.
# def add(a, *b): # The general wrtting for the Arbitrary Arguments is "args".
#     # print(a + sum(b)) # Here "sum" is a built-in function that returns the sum of all elements in an iterable.
#     temp = a
#     for i in b:
#         temp += i
#     print(temp)

# add(2, 4, 7, 2, 8, 2, 0, 5, 2, 5)
# Here except first value remaining all values store's in "*b" in a tuple format.
# In Python Method Overloading is not possible. But we can achive through Arbitrary Arguments.
# Some Disadvantages of Arbitrary Arguments.

# Keyword Arbitrary Arguments => # The general wrtting for the Key Arbitrary Arguments is "kargs". And shown as "**"
# Arbitrary Arguments are in the tuple format.

def connect_to_db(*args):
    print(args)

connect_to_db("localhost : 3300", 234, "2345", "3366")

# # In Keyword Arbitrary Argument we can assign value to key.
def connect_to_db2(**kargs):
    print(kargs)
# Keyword Arbitrary Arguments are in the dictionary format.

connect_to_db2(db_loc = "localhost : 3300", db_pool = 234, db_password = "2345", db_port = "3366")






# Difference between Arbitrary Arguments and Keyword Arbitrary Arguments
# 1. Arbitrary Arguments are in the tuple format and Keyword Arbitrary Arguments are in the dictionary format.
# 2. In Arbitrary Arguments we cannot assign value to key but in Keyword Arbitrary Arguments we can assign value to key.
# 3. In Arbitrary Arguments we can pass any number of arguments but in Keyword Arbitrary Arguments we can pass any number of key-value pairs.
# 4. In Keyword Arbitrary Arguments we have the additional context but Arbitrary Arguments do not have the additional context.


# Return Statement

# def add(num1, num2):
#     print(num1 + num2) # Any Function without any return Statement is called a Void Function.
#     # If we want to return a value from a function then we need to use the return
    
# def add2(num1, num2):
#     return num1 + num2 # This Function is called a Non-Void Function because it returns a value.


# add(2, 5)
# result = add2(4, 5)
# print(result)  # This will print the result of the addition

# def multiply(a, b):
#     print(a * b)
#     return a * b
    
# r1 = multiply(2, 5)  # This will print the result of the multiplication
# print(r1)

# print(multiply(2, 5))

# def num_check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# n = int(input("Enter a number: "))
# r2 = num_check(n)
# print(r2)

# def simple_calc(a, b):
#     return a + b, a - b, a * b

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# # print(type(simple_calc(num1, num2)))  # This will print the type of the returned value
# re1 = simple_calc(num1, num2)
# print(re1)

# Return statement once executed can be considered as the end of function call.


# Return Statement Properties
# 1. Return Statemwnt can be used to execpt value from the function.
# 2. Using Return Statement we can return multiple values. Eg:- return a + b, a - b, a * b
# 3. Once the return statement is executed then the function call is end.

# def simple_func():
#     print("bcdkcbd")
#     print("jdjnc f")
#     return 5
#     print("vhsbvs")
#     print(" vsjvndslns") # This will not be executed
    
# res1 = simple_func()
# print(res1)

# def check_ur_knowledge(num1):
#     for i in range(1, num1):
#         print(i)
#         if i == 9:
#             return
#     return 55

# print(check_ur_knowledge(22))  # This will print numbers from 1 to 9 and then return 55

def add(a, b):
    return a + b

result = add(3, 5)   # store the returned value in 'result'
print(result)        # prints 8

# You can now use 'result' anywhere else
double = result * 2
print(double)        # prints 16
