# prime_number function - returns True of False
# input1 = 200
# input2 = 400

# Method 5
# def check_prime(num1):
#     if num1 <= 1:
#         return False
#     for i in range(2, int(num1 ** 0.5) + 1):
#         if num1 % i == 0:
#             return False
    
#     return True

# input1 = int(input("Enter first number : "))
# input2 = int(input("Enter second Number : "))

# for i in range(input1, input2 + 1):
#     # res = check_prime(i)
#     # if res == True:
#     #     print(i)
#     if check_prime(i):
#         print(i)

# Fibnocci numbers => print first n fib numbers
# Fibnicci Numbers
# 0 1 1 2 3 5 8 13

# n = 10
# num1, num2 = 0, 1
# for i in range(0, n):
#     print(num1, end = " ")
#     new_num = num1 + num2
#     num1 = num2
#     num2 = new_num
    
# Armstrong Number =>
# 153
# 1634

# 1 + 125 + 27 => 153
# 1 + 1296 + 81 + 256 => 1634

# num1 = 153
# original_num1 = num1
# sum = 0

# while num1 > 0:
#     rem = num1 % 10
#     sum += rem ** 3
#     num1 //= 10
    
# print(sum) # 1 ** 3 + 5 ** 3 + 3 ** 3
# if sum == original_num1:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

num1 = 1634
original_num1 = num1
sum = 0
n = len(str(num1))

# To find number of digits in the number - 2 ways
# String conversion
# using while loop again

while num1 > 0:
    rem = num1 % 10
    sum += rem ** n
    num1 //= 10
    
print(sum) # 1 ** 3 + 5 ** 3 + 3 ** 3
if sum == original_num1:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")




# prime number function - return true or false
# input1 = 200
# input2 = 400

# def check_prime(num1):
#     if num1 <= 1:
#         return False
    
#     for i in range(2, int(num1 ** 0.5) + 1):
#         if num1 % i == 0:
#             return False
    
#     return True

# input1 = int(input("Enter first number : "))
# input2 = int(input("Enter second Number : "))

# for i in range(input1, input2 + 1):
#     # res = check_prime(i)
#     # if res:
#     #     print(i)
#     if check_prime(i):
#         print(i)

# Fibonacci number

# n = 10
# num1, num2 = 0, 1
# for i in range(0, n):
#     print(num1)
#     new_num = num1 + num2
#     num1 = num2
#     num2 = new_num

# Armstrong number
# 153
# 1634

# num1 = 153
# original_num1 = num1
# sum = 0
# n = len(str(original_num1))

# To find number of digits in the number - 2 ways
# String Conversion
# Using while loop again

# while original_num1 > 0:
#     rem = original_num1 % 10
#     sum += rem ** n
#     original_num1 = original_num1 // 10

# print(sum) # 1 ** 3 + 5 ** 3 + 3 ** 3
# if sum == num1:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")