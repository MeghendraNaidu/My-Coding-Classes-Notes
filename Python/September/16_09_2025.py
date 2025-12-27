# Bubble Sort
# Sorting =>

list1 = [10, -2, 45, 67, 81, 100, -200]
#[-200, -2, 10]
# [-2, 10, 45, 67, 81, -200, 100]

# O(n square)
# for i in range(0, len(list1)-1):
#     for j in range(0, len(list1) - 1):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     print(list1)
    
# for i in range(0, len(list1)-1):
#     for j in range(0, len(list1) - 1 - i):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     print(list1)
    
# 1st iteration => j = 0 => ignore 0 elements
# 2nd => j = 1 =>ignore 1 elements
# 3rd => j = 2 =>ignore 2 elements
# 4th => j = 3 =>ignore 3 elements

list1 = [-2, -200, 10, 45, 67, 81, 100]
# O(n * n)
# O(n * log)
for i in range(0, len(list1)-1):
    flag = True
    for j in range(0, len(list1) - 1 - i):
        if list1[j] > list1[j + 1]:
            flag = False
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
    if flag == True:
        break
    print(list1)