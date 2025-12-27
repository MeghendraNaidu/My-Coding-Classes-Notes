# Fuctions => 
# It is a block of code, which gets executed whenever you call it.


# def calc_volume():
#     print('Caculating volume of sphere')
#     print((4/3) * 3.14 * (10 ** 3))
#     print("Calculated Volume")
    
# print('Someother Operation')
# calc_volume()
# print("operations")
# calc_volume()

# def calc_volume(r, pie): # Here "r" is called Parameters
#     print('Caculating volume of sphere')
#     print((4/3) * pie * (r ** 3))
#     print("Calculated Volume")
    
# print('Someother Operation')
# calc_volume(10, 3.14) # Here "10" is called Arguments
# print("operations")
# calc_volume(15, 2.14)

# def simple_calculator(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     if b != 0:
#         print(a / b)
#         print(a // b)
#         print(a % b)
#     else:
#         print("Divsion by zero is not possible")
    
# simple_calculator(10, 20)
# simple_calculator(5, 10)
# simple_calculator(20, 30)

# Table
# def table_of(n):
#     for i in range(1, 11):
#         print(n, "X", i, "=", n * i)
        
# table_of(7)
# table_of(4)

# def sum_of(n):
#     # n = 10
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     print(sum)
    
# sum_of(10)

# def fact_of(n):
#     # n = 10
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# fact_of(10)

# n = 16
# for i in range(2, n):
#     if n % i != 0:
#         print("prime number")
#         break
#     else:
#         pass


# n = int(input("Enter a Number: "))
# for i in range(2, n):
#     if n % i != 0:
#         print("prime number")
#         break
#     else:
#         print("Not a prime")