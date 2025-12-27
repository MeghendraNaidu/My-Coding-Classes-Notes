# Lambda Functions => 

# example = lambda a, b, c, d: a + b - c * d
# print(example(2, 3, 5, 6))

# example = 50
# function = lambda a : a ** 2
# function = lambda : "Good Moring"

# Higher Order Functions =>
# Map, Filter and reduce

# Map
# map(function, iterable)
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(list(map(lambda x : x ** 3, [3, 4, 6, 7, 11, -32])))


# print(list(map(square, [3, 4, 6, 7, 11, -32])))
# print(list(map(cube, [55, 66, -6, 7, 11,  32])))

# Filter => 
# filter(function, iterable)

# print(list(filter(lambda x : x % 5 == 0 or x % 3 == 0, [1, 3, 5, 8, 9, 10, 15, 17])))


# Reduce => 
# reduce(function, iterable)

from functools import reduce

print(reduce(lambda x, y : x + y, [1, 2, 5, 7, 11, -10]))
print(reduce(lambda x, y : x * y, [1, 2, 5, 7, 11, -10]))

list1 = ['string1', 'string2', 'string3']
print(reduce(lambda x, y : x + y, list1))

print(reduce(lambda x, y : x if x > y else y, [1, 2, 5, 7, 11, -10]))
print(reduce(lambda x, y : x if x < y else y, [1, 2, 5, 7, 11, -10]))


def check_even(x):
    if x % 2 == 0:
        return True
    else: 
        return False