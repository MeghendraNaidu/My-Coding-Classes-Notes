# For else and While else


# fro i, j in enumerate(list1):


# Comprehensions

# list1 = [ i * 2  for i in range(1, 10)]
# print(list1)

y_vals = [ 3 * x + 2  for x in range(1, 21)  if x % 2 == 0]

# [expression, for, varaible, iterable, condition]

y_vals = [3 * x + 2 if x % 2 == 0 else 3 * x + 5 for x in range(1, 21)]


# aaabddcca
# a3b1d2c2a1


# Unpacking

# Extended Unpacking