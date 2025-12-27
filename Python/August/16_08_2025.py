# Nested For Loops: A loop inside another loop
# For refference in collection:
# Outer For loop Statement
# for refference in collection:

# for i in range(1, 6):
#     for j in range(1, 11):
#         print(f'{i} X {j} = {i * j}')
#     print()
    
# l = [[1, 2, 3], [3, 4, 5], [4, 7, 8]] # 6, 12, 19
# # l1 = []

# for i in l:
#     sum = 0
#     for j in i:
#         sum += j
#     # l1.append(sum)
# # print(l1)
#     print(sum)

n = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()