# Matrix => 
list1 = [
    [10, 20, 30], 
    [31, 42, 55], 
    [44, 21, 23]
]
# sum = 0

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if i == j:
#             sum += list1[i][j]
#             print(list1[i][j], end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# print(sum)

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if j == 2:
#             print(list1[i][j], end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if j == 0 or i == 0:
#             print(list1[i][j], end = " ")
#         else:
#             print(" ", end = " ")
#     print()

list1 = [
    [10, 20, 30, 44, 55], 
    [31, 42, 55, 44, 55], 
    [44, 21, 23, 44, 55],
    [31, 42, 55, 44, 55],
    [31, 42, 55, 44, 55]
]

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if j == 0 or i == 0 or i == len(list1) - 1 or j == len(list1[i]) - 1:
#             print(list1[i][j], end = " ")
#         else:
#             print("  ", end = " ")
#     print()

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if i == j or j == 0 or i == 0 or i == len(list1) - 1 or j == len(list1[i]) - 1:
#             print(list1[i][j], end = " ")
#         else:
#             print("  ", end = " ")
#     print()


for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j or j == 0 or i == 0 or i == len(list1) - 1 or j == len(list1[i]) - 1 or i + j == len(list1) - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

# n = 5

# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()