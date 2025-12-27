# Shallow Copy
list1 = [3, 4, 5, 7, [1, 2, 3]]
list2 = list1.copy()
list2[4][2] = 35
print(list1)
print(list2)

# Deep Copy
import copy
list3 = copy.deepcopy(list1)
list3[4][2] = 45
print(list3)
print(list1)


# Dictionary Inbuilt Functions

dict1 = {'k1' : 'v1', 'k2' : 'v2', 'k3' : 'v3'}

# 1. get(key, default = None)
d = {'name' : 'Manoj', 'age' : 25}
# print(d.get('name', 'N/A'))
# print(d.get('gender', 'N/A'))
# print(d.get('class'))
# print(d.get('age'))

# 2. keys()
d = {'a' : 1, 'b' : 2}
# print(list(d.keys()))
# print(d.keys())

# 3. values()
# print(list(d.values()))
# print(d.values())

# 4. items()
d = {'a' : 1, 'b' : 2}
# for k, v in d.items():
#     print(k, v)

# 5. update([other])
# d.update({'c' : 3})
# print(d)
# d.update({'a' : 5})
# print(d)
d.update([('a', 9), ('d', 4), ('e', 1)]) # For updating and adding multiple values we use this values.
print(d)

# 6. pop(key, default)
print(d.pop('e', 'Not Found'))
print(d.pop('f', 'Not Found'))

# 7. popitme()

# 8. clear()

# 9. copy()

# 10. fromkeys(keys, value = None)

# 11. zip(keys, values)

keys = ['a', 'b', 'c']
values = [1, 2]
print(dict(zip(keys, values)))
