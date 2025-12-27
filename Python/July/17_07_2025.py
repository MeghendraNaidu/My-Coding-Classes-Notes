# Control Statements
# 1. Condition Statements => if, else, elif
# 2. Loop Statements => for, while
# 3. Jump Statements => break, continue, pass

# 1. Condition Statements
# Indendation is important in Python

# Age = 19
# if Age >= 18:
#     print("I can vote")
# else:
#     print("I cannot vote")

# even or odd
# num1 = int(input("Enter a Number: "))
# if num1 % 2 == 0:
#     print(f'{num1} is an Even Number')
# else:
#     print(f'{num1} is an Odd Number')

# Positive or Nagative 
# If we have Multiple if else inside the if else it is called Nested if else
num1 = int(input("Enter a Number:"))
# if num1 > 0:
#     print("The Given Number is Positive")
# else:
#     if num1 == 0:
#         print("The Number is Zero")
#     else:
#         if num1 == -1:
#             print(f'The Given Number is {num1}')
#         else:
#             print("The Given Number is Negative")

if num1 > 0:
    print("The Given Number is Positive")
elif num1 == 0:
    print("The Number is Zero")
elif num1 == -1:
    print(f'The Given Number is {num1}')
else:
    print("The Given Number is Negative")



# Calculator

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter Sysmbol: ")

# if op == '+':
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '*':
#     print(num1 * num2)
# elif op == '/':
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Error: Division by zero")
# elif op == '%':
#     if num2 != 0:
#         print(num1 % num2)
#     else:
#         print("Error: Division by zero")
# elif op == '//':
#     if num2 != 0:
#         print(num1 // num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid operator")