# 1. Print number from 1 to n.
# n = int(input("Enter a Number: "))
# for i in range(1, n + 1):
#     print(i, end = " ")

# 2. Print number from m to n.
# m = int(input("Enter a Number: "))
# n = int(input("Enter a Number: "))
# for i in range(m, n + 1):
#     print(i, end = " ")

# 3. Print number from m to n in reverse.
# m = int(input("Enter a Number: "))
# n = int(input("Enter a Number: "))
# for i in range(m, n - 1, -1):
#     print(i, end = " ")

# 4. Sum of n natural number.
# n = int(input("Enter a Number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# 5. Factorial of a number
# n = int(input("Enter a Number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# 6. Factors of a Number.
# num = [6, 12, 18, 24]
# for i in num:
#     if num % i == 0:
#         print(i)

# 7. Count of Factors

# 8. Check Prime Number
# n = 16
# for i in range(2, n):
#     if n % i == 0:
#         print("It is a Prime")
#     else:
#         print("It is not a Prime")

# 9. Print number from 1 to 100 Even numbers.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end = " ")
#     else:
#         pass

# 10. Print number from 1 to 100 Odd numbers.
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i, end = " ")
#     else:
#         pass

# 11. Count even or odd
# even_count = 0
# odd_count = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(even_count)
# print(odd_count)

# sum = 0
# for i in range(7):
#     sum += i
# print(sum)

# 12. Armstrong
# num = "1534"
# num1 = len(str(num))
# sum = 0
# for i in num1:
#     digit = i % 10
#     sum *= 10 + digit
#     num1 //= 10
# print(sum)

# 13. Reverse String
# str1 = "Hello"
# rev_str = ""
# for i in str1:
#     rev_str = i + rev_str
# print(rev_str)

# 14. Palindrome
# str1 = "Hello"
# str2 = str1
# rev_str = ""
# for i in str1:
#     rev_str = i + rev_str
# if rev_str == str2:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")

# n = 100
# for i in range(1, n):
#     if (1 <= i <= 10) or (21 <= i <= 30) or (41 <= i <= 50) or (61 <= i <= 70) or (81 <= i <= 90):
#         print(i, end = " ")
#     else:
#         pass

# str1 = "hello world"
# str2 = "python is feature"
# vowels = "aeiouAEIOU"
# count = 0
# for i in str1, str2:
#     if i in vowels:
#         print(i)
#         count += 1
# print(count)
