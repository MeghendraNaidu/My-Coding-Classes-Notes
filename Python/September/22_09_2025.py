# Find the missing digits in a number

# Sum of elements in nested list

# Method 1 method for copying list
import copy
list1 = [20, 15, 26, 2, 98, 6]
list2 = copy.deepcopy(list1)

# Method 2 method for copying list
list1 = [20, 15, 26, 2, 98, 6]
list2 = sorted(list1) # O(nlogn)
output = []

# Normal method using in built method

# for i in list1:
#     output.append(list2.index(i) + 1)
# print(output)

# Method 2 Using linear search

for i in list1:
    for j in range(len(list2)): 
        if i == list2[j]:
            output.append(j + 1)
            
print(output)


# Method 3 method for copying list
list1 = [20, 15, 26, 2, 98, 6]
list2 = []
for i in list1:
    list2.append(list1)