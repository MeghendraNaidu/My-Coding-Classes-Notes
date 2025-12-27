# Permutationas of a String
# str1 = "ABC"
# for i in str1:
#     print(i, end = " ")

# 11. Prime Number Check
# n = int(input("Enter a Number: "))
# for i in range(2, n + 1):
#     if n % i != 0:
#         print("It is a prime")
#         break
#     else:
#         print("It is Not a prime")

# 15. Reverse a String
# str1 = "hello"
# rev_str = ""
# for i in str1:
#     rev_str = i + rev_str
# print(rev_str)

# str1 = "hello"
# print(str1[:: -1])

# 16. Check for Palindrome String
# str1 = "madam"
# rev_str = ""
# str2 = str1
# for i in str1:
#     rev_str = i + rev_str
# if rev_str == str2:
#     print("It is a Palindrome")
# else:
#     print("It is Not a Palindrome")

# 20. Reverse a Number
# num1 = 123
# num2 = 0
# while num1 > 0:
#     digits = num1 % 10
#     num2 = num2 * 10 + digits
#     num1 = num1 // 10
# print(num2)

# 21. Palindrome Number Check
# num1 = 121
# num2 = num1
# rev_num = 0
# while num1 > 0:
#     digits = num1 % 10
#     rev_num = rev_num * 10 + digits
#     num1 = num1 // 10
# if rev_num == num2:
#     print("It is a Palindrome")
# else:
#     print("It ia Not a Palindrome")

# 22. Count Vowels in String
# str1 = "apple"
# vowels = "aeiouAEIOU"
# count = 0
# for i in str1:
#     if i in vowels:
#         count += 1
#     else:
#         pass
# print(count)

# 23. Count Consonants in String
# str1 = "apple"
# vowels = "aeiouAEIOU"
# count = 0
# for i in str1:
#     if i not in vowels:
#         count += 1
#     else:
#         pass
# print(count)

# 24. Count Vowels and Consonants
# str1 = "apple"
# vowels = "aeiouAEIOU"
# vowels_count = 0
# conso_count = 0
# for i in str1:
#     if i in vowels:
#         vowels_count += 1
#     else:
#         conso_count += 1
# print("Vowels:",vowels_count)
# print("Consonants:",conso_count)

# 29. Fibonacci Series
# n = 5
# a, b = 0, 1
# for i in range(n):
#     print(a, end = " ")
#     a, b = b, a + b