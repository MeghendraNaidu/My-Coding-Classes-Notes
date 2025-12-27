# list1 = [-201, -203, -204, -205]

# current_max = float("-inf") # 0 cannot be taken initial value
# current_min = float("inf")

# for i in list1:
#     sum += i
    
#     if i > current_max:
#         current_max = i

#     if i < current_min:
#         current_min = i


# print(current_max)

# Revese a list

# Method 1
#list1.reverse()

# Method 2
list1 = [10, 20, 30, 40, 50]

# # print(list1[ : : -1])
# list1 = list1[ : : -1]
# print(list1)

# Method 3
# for i in list1:
#     print(i)

# for ind in range(0, len(list1)):
#     # print(ind)
#     print(list1[ind])

# new_list = []
# for i in list1:
#     new_list.insert(0, i)
# list1 = new_list
# print(list1)

# new_list = []
# for ind in range(len(list1) - 1, -1, -1):
#     # print(ind)
#     # print(list1[ind])
#     new_list.append(list1[ind])
# list1 = new_list
# print(list1)

list1 = [10, 20, 30, 40, 50]

low = 0
high = len(list1) -1

while low < high:
    list1[low], list1[high] = list1[high], list1[low]
    low += 1
    high -= 1
    
print(list1)


# reverse a string =>
# sum of digits => [123, 456, 78, 91, 56]
# [6, 15, 15, 10, 11]

# max digit in a number # 471
# [123, 456, 78, 91, 56] => [3, 6, 8, 9, 6]


# Bubble sort
# Linear search
# Binary search