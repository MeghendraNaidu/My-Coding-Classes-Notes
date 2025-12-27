n = 7

# for i in range(n):
#     for sp in range(n - i - 1):
#         print(" ", end = "")
        
#     for j in range(n):
#         if i >= j:
#             print("*", end = " ")
#     print()


# for i in range(n):
#     for sp in range(i):
#         print(" ", end = "")
    
#     for j in range(n):
#         print("*", end = " ")
#     print()


# for i in range(n):
#     for j in range(n):
#         if (i >= j and i + j <= n - 1) or (i <= j and i + j >= n - 1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(n):
#     for j in range(n):
#         if (i > j and i + j < n - 1) or (i < j and i + j > n - 1):
#             print(" ", end = " ")
#         else:
#             print("*", end = " ")
#     print()


# curr = 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(curr, end = " ")
#             curr += 1
#         else:
#             print(" ", end = " ")
#     # curr += 1
#     print()



# for i in range(n):
#     curr = 1
#     for j in range(n):
#         if i >= j:
#             print(curr, end = " ")
#             curr += 1
#         else:
#             print(" ", end = " ")
#     print()


# for i in range(n):
#     for sp in range(n - i - 1):
#         print(" ", end = "")
        
#     for j in range(n):
#         if i >= j:
#             print(i + 1, end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# visible = True

# for i in range(n):
#     if i % 2 == 0:
#         visible = True
#     else:
#         visible = False
        
#     for j in range(n):
#         if (i >= j and i + j <= n - 1):
#             if visible == True:
#                 print("*", end = " ")
#                 visible = False
#             else:
#                 print(" ", end = " ")
#                 visible = True
#         else:
#             print(" ", end = " ")
#     print()


visible = True

for i in range(n):
    if i % 2 == 0:
        visible = True
    else:
        visible = False
        
    for j in range(n):
        if (i >= j and i + j <= n - 1):
            if visible == True:
                print(1, end = " ")
                visible = False
            else:
                print(0, end = " ")
                visible = True
        else:
            print(" ", end = " ")
    print()