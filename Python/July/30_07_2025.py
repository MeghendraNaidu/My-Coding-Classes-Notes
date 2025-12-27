# Practice

# Write a program to classify a character entered by the user as a vowel, consonant, or neither.
# str1 = input("Enter a Character : ")
# str2 = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
# str3 = "0123456789"
# if len(str1) > 1 or len(str1) == 0:
#     print("Invalid Inpput")
# else:
#     if str1 in str2:
#         print("Given character is Vowel")
#     # elif str1.isalpha():
#     elif str1 in str3:
#         print("Given Character is special character")
#     else:
#         print("Given character is consonant")

# Write a program to check if three sides length form a valid triangle.
# num1 = int(input("Enter first side: "))
# num2 = int(input("Enter second side: "))
# num3 = int(input("Enter third side: "))
# if (num1 + num2 > num3) and (num2 + num3 > num1) and (num1 + num3 > num2):
#     print("Is a Valid Triangle")
# else:
#     print("It is not a valid Triangle")

# Print all numbers from 1 to 100 using a for loop.
# for i in range(1, 101):
#     print(i, end = " ")

# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
# n = int(input("Enter n Natural Number : "))
# s = 0
# for i in range(1, n+1):
#     # s= n*(n+1)/2
#     s += i
# print(s)

# Print all even numbers between 1 and 50 using a while loop.
# i = 2
# while i <= 50:
#         print(i)
#         i += 2

# Write a program to display the multiplication table of a given number. First 20
# n = int(input("Enter a table : "))
# i = 1
# while i < 21:
#     print(n, "x", i, "=", n * i)
#     i += 1

# Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.

# Write a program to count the number of digits in a given number using a while loop.
# n = int(input("Enter a Number : "))
# s = 1
# count = 0
# while n > 0: 
#     n = n // 10
#     count += 1
# print(count)

# Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.
# while True:
#     n = int(input("enter a negative number: "))
#     if n < 0:
#         print("It is a Negative Numver")
#         break
#     else:
#         print(f"You have Entered {n}")

# Print the first 10 terms of the Fibonacci series using a for loop.
# n = int (input("Enter 10 Terms: "))
# a,b = 0,1
# count = 0
# for i in range(1, 11):
#     print(a, end = " ")
#     a,b = b, a+b
#     count += 1

# Check if a given number is a prime number using a for loop.

# Write a program to calculate the factorial of a number using a while loop.

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

# Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.

# Implement a basic login system where the user has three attempts to enter the correct password using a loop.