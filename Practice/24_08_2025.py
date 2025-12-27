# Set Inbuilt Functions

set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}

# Add Function = Add an element to the set.
set1.add(9)
print(set1)

# Remove Function = Remove an element from the set. If the element is not found in set it raise to keyError.
set1.remove(3)
print(set1)
# set1.remove(10)  # KeyError: 10
# print(set1)

# Discard Function = Removing an element from the set. If the element is not found in set it does not raise to KeyError.
set1.discard(4)
print(set1)
set1.discard(11) # does not raise to KeyError: 11
print(set1)

# Pop Function = Removing any element present in the set. But it won't remove the particular element because set is unordered.
set1.pop()
print(set1)
set1.pop()
print(set1)

# Clear Function = Removing all elements from the set.
set1.clear()
print(set1)

# Union Function = Combining two sets. It removes the duplicate elements.
set3 = set1.union(set2) # Here set1 union set and set2 union set1 are both same.
print(set3)
set3 = set2.union(set1)
print(set3)

# Intersection Function = It returns the common elements from both sets.
set3 = set1.intersection(set2) # Here set1 intersection set and set2 intersection set1 are both same.
print(set3)
set3 = set2.intersection(set1)
print(set3)

# Difference Function = It returns the elements present in first set but not in second set.
set3 = set1.difference(set2) # Here set1 difference set2 and set2 difference set1 are both different.
print(set3)
set3 = set2.difference(set1) 
print(set3)

# Symmetric Difference Function = It returns the elements present in either set elements. But it will remove the duplicate elements from the both sets.
set3 = set1.symmetric_difference(set2) # Here set1 symmetric_difference set2 and set2 symmetric_difference set1 are both same.
print(set3) 
set3 = set2.symmetric_difference(set1)
print(set3) 