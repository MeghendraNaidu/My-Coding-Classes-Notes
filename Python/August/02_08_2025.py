# def greater(num1, num2, num3): # Here in brackets are called Parameters
#     if num1 > num2 and num1 > num3:
#         print(f"{num1} is Greater")
#     elif num2 > num1 and num2 > num3:
#         print(f"{num2} is Greater")
#     else:
#         print(f"{num3} is Greater")


# greater(9, 5, 6) # Here in brackets are called Arguments
# greater(11, 20, 15)
# greater(10, 20, 40)

# Positional Arguments # greater(10, 20, 40) this is called Positional Arguments

# Keyword Arguments means directly assining values to keys Eg:- greater(num1 = 9, num2 = 8, num3 = 5) Here value assign in arguments

# Default Arguments directly assign value in Parameter is called default arguments Eg:- def greater(num1 = 10, num2, num3 = 15):
# or After assigning a value in parameters(Here value is default) we can also take another value in Arguments

# Errors in code
# parameter without a default follows parameter with a default

# We can not write non - default argument before a default arguments. Eg:- def greater(num1 = 10, num2, num3): Like this
# Default Arguments should be in last place and non default should be in first place.
# or first we need to write all non default arguments and then at last we need to write default arguments.

# we can combine and write positional arguments and keyword arguments
# if we want to combine both first we need write the all Positional Arguments and at last we need to write Keyword Arguments.

# greater(9, 5, 6)
# greater(9, num2 = 5, 6)

# Arbitrary Arguments

# def add(a , b):
#     print(a + b)

# def add(a, b, c):
#     print(a + b + c)

# def add(a, b, c, d):
#     print(a + b + c + d)
    
# add(2, 3)
# add(2, 3, 4)
# add(2, 3, 4, 5)
# This is called Method Overloading this is not support in "python"

# Arbitrary Arguments
# def add(a ,* b): # Here "*" is Called Arbitrary Arguments
#     print(a)
#     print(b)
#     # print(a + sum(b))

# add(2, 3)
# add(2, 3, 4)
# add(2, 3, 4, 5)
# Methos Overloading is not supported in Python but in directly we can use "Arbitrary Arguments"


# n = int(input("Enter a Number : "))
# for i in range(2, n):
#     if n % i == 0:
#         print("It is Not a Prime Number")
#         break
# else:
#     print("It is a Prime Number")

# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print('not prime')
#         break
# else:
#     print('prime')

# what is prime number
# A prime number is a natural number greater than 1 that is not divisible by any other numbers except for 1 and itself.