n = 5
n1 = n // 2

# A Letter
# for i in range(n):
#     for j in range(n):
#         if ((j == 0 or j == n -1) and i != 0) or (i == 0 and j > 0 and j < n - 1) or ( i == n // 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# B Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0 and j < n - 1) or (i == n - 1 and j < n - 1) or (i == n1 and j < n - 1) or ((j == n -1 and i != 0) and (j == n - 1 and i != n // 2) and (j == n - 1 and i != n - 1)):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# C Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0 and i != 0 and i != n - 1) or (i == 0 and j != 0) or (i == n - 1 and j != 0):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# D Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0 and j < n - 1) or (i == n - 1 and j < n - 1) or ((j == n - 1 and i != 0) and (j == n - 1 and i !=  n - 1)):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# E Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0) or (i == n - 1) or (i == n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# F Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0) or (i == n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# G Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0 and j > 0) or (j == 0 and i > 0 and i < n - 1) or (i == n - 1 and j > 0 and j < n - 1) or (j == n - 1 and i < n - 1 and i >= n1) or (i == n1 and j >= n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# H Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (j == n - 1) or (i == n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# I Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0) or (i == n - 1) or (j == n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# J Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0) or (j == n1 and i < n - 1) or (i == n - 1 and j < n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# K Letter
# for i in range(n):
#     for j in range(n):
#         if (j == n1 - 1) or (i + j == n - 1 and i != n - 1) or (i == j and i != 0):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# L Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# M Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (j == n - 1) or (i == j and i == j <= n1) or (i + j == n - 1 and i -j <= n1 - 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# N Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (j == n - 1) or (i == j):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# O Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0 and i > 0 and i < n - 1) or (j == n - 1 and i > 0 and i < n - 1) or (i == 0 and j > 0 and j < n - 1) or (i == n - 1 and j > 0 and j < n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# P Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0 and j < n - 1) or ( i == n1 and j < n - 1) or (j == n - 1 and i > 0 and i < n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# Q Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0 and i > 0 and i < n - 1) or (j == n - 1 and i > 0 and i < n - 1) or (i == 0 and j > 0 and j < n - 1) or (i == n - 1 and j > 0 and j < n - 1) or (i == j and i == j >= n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# R Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (i == 0 and j < n - 1) or ( i == n1 and j < n - 1) or (j == n - 1 and i > 0 and i != n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# S Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0 and j > 0) or (i == n - 1 and j < n - 1) or (i == n1 and j > 0 and j < n - 1)or (j == 0 and i > 0 and i < n1) or (j == n - 1 and i < n - 1 and i > n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# T Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0) or (j == n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# U Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0 and i < n - 1) or (j == n - 1 and i < n - 1) or (i == n - 1 and j > 0 and j < n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# V Letter
for i in range(n):
    for j in range(n * 2):
        if j == i or j == (2 * n - 2) - i:
        # if (i == j and i == j <= n1) or (i + j == n - 1 and i - j <= n1 -2):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
    
# W Letter
# for i in range(n):
#     for j in range(n):
#         if (j == 0) or (j == n - 1) or (i == j and i == j >= n1) or (i + j == n - 1 and i - j >= n1 - 2):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
    
# X Letter
# for i in range(n):
#     for j in range(n):
#         if (i == j) or (i + j == n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# Y Letter
# for i in range(n):
#     for j in range(n):
#         if (i == j and i == j <= n1) or (i + j == n - 1 and i - j <= n1 -2) or (j == n1 and i >= n1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
    
    
# Z Letter
# for i in range(n):
#     for j in range(n):
#         if (i == 0) or (i == n - 1) or (i + j == n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

