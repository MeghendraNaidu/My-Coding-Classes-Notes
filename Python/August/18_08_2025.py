# Scope => Local, Global, Enclosed and Builtin

# num1 = 10
# def check_function():
#     num2 = 10
#     print(num2)
#     def inner_function():
#         num3 = 20
#         print("Hi")
    
# check_function()
# print(num2)
# inner_function()

# Global Keyword
# num1 = 10
# def preference():
#     global num1
#     num1 = 20
#     print(num1)
    
# preference()
# print(num1)

# Globals Function
# num1 = 10
# def preference():
#     num1 = 20
#     globals()['num1'] = 50
#     print(num1)
    
# preference()
# print(num1)
 
# num2 = 10
# def first_function():
#     num2 = 20
#     def second_function():
#         nonlocal num2
#         num2 = 40
#         print("Hi")
#         print(num2)
        
#     second_function()
#     print(num2)
    
# first_function()

# num2 = 10
# def first_function():
#     num2 = 20
#     def second_function():
#         num2 = 20
#         def third_function():
#             nonlocal num2
#             num2 = 30
#             print(num2)
            
#         third_function()
#         print(num2)
        
#     second_function()
#     print(num2)
    
# first_function()

# Scope => In which area it can be use
# Lifetime  => how much time it can be in active



# Lambda Functions => anonymous means it don't have any name. It is a one line functions

def add(a, b):
    return a + b

print(add(2, 3))


example_function = lambda a, b: a + b
print(example_function(2, 3))
example_function = 50
print(example_function(2, 3))