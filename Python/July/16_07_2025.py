# Control Statements
# Control statements allow you to control the flow of execution in your program.
# They can be used to make decisions, repeat actions, or handle exceptions.
# 1. Conditional Statements
# Conditional statements allow you to execute code based on certain conditions.
# It Check the condition if condition is satisfied or not Boolean Trues=> 1, False=> 0.
# $ Types Simple if, else, elif, nested if.
# Example of a simple if statement
# num = 10
# if num > 5:
#     print("Number is greater than 5")

# num1 = 63
# if num1 > 40 and num1 % 7 == 0:
#     print(f'{num1} power is {num1 ** 2}')

# list1 = [1, 2, 3, 4, 5]
# if 4 in list1:
#     print("4 is present in list1")

#if else: when ever we have one condition two diff task
# if condition:
#            set of Statements
# else:
#            set of Statements
# num1 = 27
# if num1 % 2 == 0:
#     print(f"{num1} is an even number")
# else:
#     print(f"{num1} is an odd number")

# Age = int(input("Enter the Person Age:"))
# if Age >= 18:
#     print("The Person can Vote")
# else:
#     print("The Person can not Vote")

# elif: we have more then one condition


# a = int(input("Enter 1st Person Age:"))
# b = int(input("Enter 2nd Person Age:"))
# c = int(input("Enter 3rd Person Age:"))
# if a >= b and a>= c:
#     large = a
#     print(large)
# elif b >= a and b >= c:
#     large = b
#     print(large)
# else:
#     large = c
#     print(large)

num1 = int(input("enter a num1 : "))
num2 = int(input("enter a num2 : "))
num3 = int(input("enter a num3 : "))


if num1 == 1 and (num2 <= 9 and num3 <= 9):
    print(num2 + num3)
elif num1 == 2 and (num2 <= 9 and num3 <= 9):
    print(num2 - num3)
elif num1 == 3 and (num2 <= 9 and num3 <= 9):
    print(num2 * num3)
elif num1 == 4 and (num2 <= 9 and num3 <= 9):
    print(num2 / num3)
else:
    print("invalid")
            


''' # This is System Given Content '''
# They are used to make decisions in your code.
# The most common conditional statements are if, else, and elif.
# Syntax:
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
# elif condition:
#     # code to execute if the previous condition is false and this condition is true
# Example:
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
# elif another_condition:
#     # code to execute if the previous condition is false and this condition is true
# 2. Looping Statements
# Looping statements allow you to repeat a block of code multiple times.
# The most common looping statements are for and while.
# Syntax:
# for variable in iterable:
#     # code to execute for each item in the iterable
# while condition:
#     # code to execute as long as the condition is true
# Example:
# for i in range(5):
#     print(i)
# while num < 20:
#     print(num)
#     num += 1