# get(key, default=None)
d = {'name' : 'Manoj', 'age' : 30}
print(d.get('name'))
print(d.get('gender', 'Not Found'))
print(d.get('class'))

# Keys()
d = {'a' : 1, 'b' : 2, 'c' : 3}
print(d.keys())
print(list(d.keys()))

# Values()
print(d.values())
print(list(d.values()))

# Items()
for k, v in d.items():
    print(k, v)

# Update()
d.update({'c': 4})
print(d)
d.update([('d', 5), ('e', 6), ('f', 7)])
print(d)

# Pop()
print(d.pop('a'))
print(d)
print(d.pop('x', 'Not Found'))
print(d.pop('y'))

# Popitem()
print(d.popitem())
print(d)
print(d.popitem())

# Clear()
d.clear()
print(d)

# Copy()
d2 = d.copy()
print(d2)

# FromKeys()
d3 = dict.fromkeys(['x', 'y', 'z'], 0)
print(d3)
d4 = dict.fromkeys(['x', 'y', 'z'], [])
d4['x'].append(1)
print(d4)

# Zip()
keys = ['x', 'y', 'z']
values = [1, 2, 3]
d5 = dict(zip(keys, values))
print(d5)

keys = ['x', 'y', 'z']
values = [4, 5]
d6 = dict(zip(keys, values))
print(d6)

keys = ['x', 'y']
values = [6, 7, 8]
d6 = dict(zip(keys, values))
print(d6)
