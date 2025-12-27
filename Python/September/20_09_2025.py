# list1 = [10, 20, 30, 30, 40, 20]
# list2 = [10, 20, 30, 40, 50, 60]

# flag = True
# for i in list1:
#     if (i not in list2) or (list2.count(i) < list1.count(i)):
#         print("Not a Subset")
#         flag = False
#         break
# if flag == True:
#     print("Is a Subset")

# Finding duplicates in the list
list1 = [10, 10, 20, 30, 10, 45, 20]

# visited = []
# duplicate = []

# for i in list1:
#     if i not in visited:
#         visited.append(i)
#     else:
#         if i in duplicate:
#             continue
#         else:
#             duplicate.append(i)
#             print(i, "is duplicate")

# {
#     10 : 3
#     20 : 2
#     45 : 1
# }

# list1 = [10, 10, 20, 30, 10, 45, 20]

# dict1 = {}

# for i in list1:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] = dict1[i] + 1
# print(dict1)

dict2 = {}
for i in list1:
    dict2[i] = dict2.get(i, 0) + 1
print(dict2)

for i, j in dict2.items():
    if j > 1:
        print(i, "is duplicate")


# duplicates digits in a given number
# 1145 => 1
# 2466 => 6
# 234624 => 2, 4

# num = 1145
# dict1 = []
# dict2 = []

# while num > 0:
#     digit = num % 10
#     if digit not in dict1:
#         dict1.append(digit)
#     else:
#         if digit not in dict2:
#             dict2.append(digit)
#     num //= 10
    
# print(dict2)

num = 234624
dict1 = {}

while num > 0:
    digit = num % 10
    if digit not in dict1:
        dict1[digit] = 1
    else:
        dict1[digit] = dict1[digit] + 1
    num //= 10

for i, j in dict1.items():
    if j > 1:
        print(i, "is Duplicate")
    
