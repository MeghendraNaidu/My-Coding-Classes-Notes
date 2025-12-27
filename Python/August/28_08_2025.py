num1 = 15651
temp = num1
# # Find no of Digits
# # sum of digits
# # And also print digits

# count = 0
# sum = 0

# while num1 > 0:
#     digits = num1 % 10
#     print(digits)
#     num1 = num1 // 10
#     count += 1
#     sum += digits

# print(count)
# print(sum)

# Reverse Number

# Input = 1564
# Output = 4651


# rev_num = 0
# while num1 > 0:
#     digits = num1 % 10
#     rev_num = rev_num * 10 + digits
#     num1 = num1 // 10
# if rev_num == temp:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")
    
# print(rev_num)

# Swapping values in 2 variables
num1 = 10
num2 = 20
# num1 = num2
# num2 = num1
# print(num1)
# print(num2)

# Method 1
# num1, num2 = num2, num1
# a, b = b, a

# Method 2
# temp = num2
# num2 = num1
# num1 = temp
# print(num1, num2)

# Method 3
num1 = 10
num2 = 20

num1 = num1 + num2 # num1 = 30
num2 = num1 - num2 # num2 = 10
num1 = num1 - num2 # num1 = 20

# Method 4 Using xor
x = 5
# print(x ^ x)
# print(x ^ 0)

num1 = 10
num2 = 20

num1 = num1 ^ num2 #10 ^ 20
num2 = num1 ^ num2 #(10 ^ 20) ^ 20 # num2 = 10
num1 = num1 ^ num2 # (10 ^ 20) ^ 10 # num1 = 20
print(num1)
print(num2)