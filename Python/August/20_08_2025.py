# Inbuilt Methods - upper, lower, isalpha
# User Defined Functions

# List Inbuilt Function = collection ordered heterogenous
list1 = [1, 2, 3, 6, [-7, -9,], 'str1']
# print(len(list1))
# print(list1[4][1])

# print(list1[5 : 4 : -1])
# print(list1 + [2, 3, 6])

# list1 = list1 + [7]
# print(list1)

# Adding Elements
# Append Inbuilt Function = 1. we cannot add multiple elements. 2. It only add in last position.
# list1.append(7)
# list1.append(9)
# list1.append([2, 3, 4])
# print(list1)

# Extend Inbuilt Function = 1. It add multiple elements and it should mention in list formate for adding. 2. It also add in last position only.
# list1.extend([71, 88, 92])
# print(list1)


# Insert Inbuilt Fuction = 1. Adding elements in particular position
# insert(index, element)
# list1.insert(0, [-3, 5, 4, 6])
# print(list1)

# Removing Elements

# list1.clear()
# print(list1)

# pop()
list1 = [1, 2, -7, 2, 2, [4, 5], -7, -7]
# elem = list1.pop() # pop is a default arguments if we don't mention index it will remove the last index elements.
# print(elem)

# remove(elem)
# list1.remove(2)
# print(list1)

# freq = list1.count(2) # It will count how many times the value repeated.

# for i in range(freq):
#     list1.remove()
# print(list1)

# print(list1.index(-7, 3, 7))
# print(list1.index(25))

list1 = list1[:: -1]

# reverse = 
list1.reverse()

# Sort
list1 = [1, -3, 91, -27, 5, 6, 5]
list1.sort() # It is for asscending order
list1.sort(reverse = True) # it is for Decending Order
print(list1)

