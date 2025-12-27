# Set Inbuilt Functions
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}

# set3 = set1.issubset(set2)
# print(set3)
# set3 = set2.issubset(set1)
# print(set3)

# set3 = set1.issuperset(set2)
# print(set3)
# set3 = set2.issuperset(set1)
# print(set3)

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)

# Operator OverLoading

# print(45 - 60)
# print(45 - (- 60 ))

# list1 = [1, 2, -32, 4, 65, 81]
# list1.sort()
# print(list1)

# Sorted

# list1 = ["ball", "apple", "elephant", "dog", "eagle"]
# list1.sort(key = len, reverse = True)
# print(list1)

# list1 = [1, 2, 5, 7, "cat", "dog"]
# list1.sort()
# print(list1) # TypeError: '<' not supported between instances of 'str' and 'int'

# list1 = [[1, 2, 3], [-3, 4, 5, 7], [0.5, 7, 19]]
# list1.sort(key = list1[0])
# print(list1) # TypeError: 'list' object is not callable

# list1 = [[1, 2, 3], [-3, 4, 5, 7], [0.5, 7, 19]]
# list1.sort(key = lambda x: x[0])
# print(list1)

# list1 = [[1, 2, 3], [1, 4, -5, 7], [0.5, 7, 19]]
# list1.sort(key = lambda x: (x[0], x[2]))
# print(list1)

# Copy 
list1 = [1, 2, 3, [5, 6, 7]]
# list2 = list1
# list1.append(5)
# print(list2)

list2 = list1.copy()
print(list1)
print(list2)
list1[1] = 99
list1[3][1] = 62
print(list1)
print(list2)


