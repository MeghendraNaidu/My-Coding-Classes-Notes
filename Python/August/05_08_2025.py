# def Number(num1):
#     if num1 > 0:
#         print("It is a Positive Number")
#     elif num1 == 0:
#         print("It is a Zero")
#     else:
#         print("It is a Negative Number")

# num1 = int(input("Enter a number : "))

# Number(num1)


# def Number(num1):
#     if num1 % 2 == 0:
#         print("It is a Even Number")
#     else:
#         print("It is a Odd Number")

# num1 = int(input("Enter a number : "))

# Number(num1)

# print("Even") if num1 % 2 == 0 else print("Odd") # It is a Tearnary Operator

# def check_even_or_odd(num1):
#     return 'Even' if num1 % 2 == 0 else 'Odd'
# num1 = int(input("Enter a Number : "))
# print(check_even_or_odd(num1))


# def Age_Check(Age):
#     if Age >= 18:
#         print("Can Vote")
#     else:
#         print("Cannot Vote")
        
# Age = int(input("Enter your Age :"))
# Age_Check(Age)

# def Age_Check(Age):
#     return "Can Vote" if Age >= 18 else "Cannot Vote"

# Age = int(input("Enter your Age : "))
# print(Age_Check(Age))

# def Greater(num1, num2):
#     # if num1 > num2:
#     #     print(num1," is Greater")
#     # elif num1 == num2:
#     #     print("Both are Equal")
#     # else:
#     #     print(num2," is Greater")
#     # print(num1) if num1 > num2 else print("Both are Equal") if num1 == num2 else print(num2)
#     return num1 if num1 > num2 else "Both are Equal" if num1 == num2 else num2

        
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))

# print(Greater(num1, num2))


# def Operations(num1, num2, op):
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         print(num1 / num2) if num2 != 0 else print("Divisio is not Possible")
#     else:
#         print("Invalid")
        
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# op = input("Enter Your Operator: ")

# Operations(num1, num2, op)

def Operations(num1, num2, op):
    # if op == "+" or op == "add":
    if op in ["+", "add"]:
        print(num1 + num2)
    # elif op == "-" or op == "sub":
    elif op in ["-", "sub"]:
        print(num1 - num2)
    # elif op == "*" or op == "mul":
    elif op in ["*", "mul"]:
        print(num1 * num2)
    # elif op == "/" or op == "div":
    elif op in ["/", "div"]:
        print(num1 / num2) if num2 != 0 else print("Divisio is not Possible")
    else:
        print("Invalid")
        
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
# op = input("Enter Your Operator: ")
op = input("Enter Your Operator: ").lower()

Operations(num1, num2, op)