# 1. Print Numbers from 1 to n
# n = 5
# for i in range(1, n + 1):
#     print(i, end = " ")

# 2. Print Numbers from m to n
# m = 3
# n = 7
# for i in range(m, n + 1):
#     print(i, end = " ")

# 3. Print Numbers from n to 1 in Reverse
# n = 5
# for i in range(n, 0, -1):
#     print(i, end = " ")

# 4. Print Numbers from n to m in Reverse
# n = 10
# m = 6
# for i in range(n, m - 1, -1):
#     print(i, end = " ")

# 5. Sum of n Natural Numbers
# n = 5
# n1 = 0
# for i in range(1, n + 1):
#     n1 += i
# print(n1)

# 6. Factorial of a Number
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# 7. Sum of m to n Numbers
# m = 3
# n = 6
# n1 = 0
# for i in range(m, n + 1):
#     n1 += i
# print(n1)

# 8. Product of m to n Numbers
# m = 2
# n = 4
# n1 = 1
# for i in range(m, n + 1):
#     n1 *= i
# print(n1)

# 9. Print Factors of a Number
# n = 6
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end = " ")

# 10. Count of Factors
# n = 6
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end = " ")
#         count += 1
# print("Count of Factors:", count)

# 11. Prime Number Check

# 12. Even Numbers from m to n
# m = 3
# n = 10
# for i in range(m, n + 1):
#     if i % 2 == 0:
#         print(i, end = " ")
#     else:
#         pass
    
# 13. Odd Numbers from m to n
# m = 3
# n = 10
# for i in range(m, n + 1):
#     if i % 2 != 0:
#         print(i, end = " ")
#     else:
#         pass

# 14. Count of Even and Odd Numbers
# m = 3
# n = 7
# even_count = 0
# odd_count = 0
# for i in range(m, n + 1):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even_Count:", even_count)
# print("Odd_Count:", odd_count)

# 15. Reverse a String
# str1 = "hello"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print(str2)

# str1 = "hello"
# print(str1[:: -1])

# 16. Check for Palindrome String
# str = "madam"
# str1= ""
# for i in str:
#     str1 = i + str1
# print(str1)
# if str1 == str:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")

# 17. Sum of Digits
# n = 123
# n1 = 0
# for i in str(n):
#     n1 += int(i)
# print(n1)

# 18. Product of Digits
# n = 123
# n1 = 1
# for i in str(n):
#     n1 *= int(i)
# print(n1)

# 20. Reverse a Number
# n = 123
# n1 = n
# rev_n = 0
# while n > 0:
#     digits = n % 10
# # print(digits)
#     rev_n = rev_n * 10 + digits
#     n = n // 10
# print(rev_n)

# 21. Palindrome Number Check
# n = 121
# n1 = n
# rev_n = 0
# while n > 0:
#     digits = n % 10
#     rev_n = rev_n * 10 + digits
#     n = n // 10
# if rev_n == n1:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")

