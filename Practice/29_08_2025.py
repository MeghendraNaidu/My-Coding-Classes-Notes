# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rev = []
# for i in list1:
#     for j in i:
#         rev.insert(0, j)

# print(rev) # And the reverse list want to store as a nested list
# nested_rev = []
# temp = []
# for i in rev:
#     temp.append(i)
#     if len(temp) == 3:
#         nested_rev.append(temp)
#         temp = [] # Reset temp for the next group
# print(nested_rev)

# Sum of List
# list1 = [1, 2, 3, 4, 5, 6]
# sum = 0
# for i in list1:
#     sum += i
# print(sum)

# Removing duplicates
# list1 = [1, 2, 3, 4, 5, 6, 4, 3, 5]
# list2 = list(set(list1))
# print(list2)


list1 = [1, 2, 3, 4, 5, 6]
add = 0
sub = 0
for i in list1:
    spi = len(list1) // 2
    list2, list3 = list1[:spi], list1[spi:]
for j in list2:
     add += j
for k in list3:
    sub -= k
print(add)
print(sub)
            
    # add += sum(list2)
    # sub -= sum(list3)
# print(sum(list2))
# print(list3)


# if (operator.add(list2) and operator.sub(list3)) or (operator.sub(list2) and operator.add(list3)):
#     print("Condition met")
#     print(list2)
#     print(list3)
# else:
#     print("Condition not met")



# Printing first value to last position
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = l1[0]
# for i in range(1, len(l1)):
#     l1[i - 1] = l1[i]
#     l1[-1] = l2
# print(l1)