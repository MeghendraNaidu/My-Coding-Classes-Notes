# WAP that keeps asking the user to enter numbers until they enter a negative number. Use a while loop
# Method 1
# while True:
#     ip_num = float(input("Enter a positive Number: "))
#     if ip_num <= 0:
#         print("Non Positive Entered")
#         break

# Method 2
# ip_num = float(input("Enter a positive number: "))
# while ip_num < 0:
#     ip_num = float(input("Enter a positive number: "))

# Reverse a number using a while loop and also an we get the sum of all the digits.
# WAP to count the number of digits in a given number using a while loop.

# we can solve this question in two ways
# 1. simple way # Method 1
# 12345
# num1 = 12345
# str1 = str(num1) # "12345"
# print(len(str1))

# sum = 0
# for i in str1:
#     sum += int(i)

# 2. Method
# 12345 => Divide with 10 => rem = 5, Q = 1234
# 1234 => rem = 4, Q = 123
# 123 => rem = 3, Q = 12
# 12 => rem = 2, Q = 1
# 1 => rem = 1, Q = 0

# num1 = 12845 # Method 2
# count = 0
# sum = 0

# while num1 > 0:
#     rem = num1 % 10
#     print(rem)
#     # que = num1 // 10
#     # num1 = que
#     num1 = num1 // 10
#     count += 1
#     sum += rem
# print(sum)
# print(count)


while True:
    op = input("Enter your Operator Symbol: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if op == "1":
        print(num1 + num2)
    elif op == "2":
        print(num1 - num2)
    elif op == "3":
        print(num1 * num2)
    elif op == "4":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Divieion by Zero Not Possible")
    else:
        print("Invalid Operator")
        break
    
    