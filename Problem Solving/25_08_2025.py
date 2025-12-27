# Patterns

# 0
# 1   3
# 1   5   13
# 2   8   21  34

# Print the first 10 terms of the Fibonacci series using a for loop.
n = 10
a,b = 0,1
count = 0
for i in range(1, 11):
    print(a, end = " ")
    a,b = b, a+b
    count += 1

# Fibonacci rigthangle triangle

# n = 10
# a, b = 0, 1
# count = 0
# for i in range(1, 5):
#     for j in range(i):
#         print(a, end = " ")
#         a, b = b, a + b
#         count += 1
#     print()


rows = 4
n = 10
a, b = 0, 1
count = 0

matrix = [[] for _ in range(rows)]

for i in range(rows):
    for j in range(i, rows):
        matrix[j].append(a)
        a, b = b, a + b
        count += 1
    print()
    
for r in matrix:
    print(" ".join(map(str, r)))
    


        
    #     ch += 1
    #     if ch > 90:
    #         ch = 65
    # print()