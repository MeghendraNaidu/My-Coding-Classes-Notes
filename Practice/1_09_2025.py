# Write a function to calculate the factorial of a number.
# def factorial(n):
#     fact = 1
#     i = 1
#     while n >= i:
#         fact *= i
#         i += 1
#     print(fact)
# factorial(5)

# Write a function to return the Fibonacci sequence up to N terms.
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(1, n + 1):
#         print(a, end = " ")
#         a, b = b, a + b
# fibonacci(10)

# Write a program to check if a year is a leap year.
# def leap(n):
#     if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
#         print(n, "is a Leap Year")
#     else:
#         print(n, "is not a Leap Year")
# leap(2004)

# n = 2000
# m = 3000
# for i in range(n, m + 1):
#     if (i % 4 == 0  and i % 100 != 0) or (i % 400 == 0):
#         print(i, end = " ")
#     else:
#         pass

# Write a program to count the number of digits in a number.
# def check(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n //= 10
#     print(count)
# check(123456)
