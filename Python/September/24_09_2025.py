# Check if the given matrix is an identity matrix
# Add 2 Matrix
# Sum odf Diagonal elements
# Matrix Multiplication

# list1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# n1 = len(list1)

list1 = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

identity = True
rows = len(list1)
column = len(list1[0])

if rows != column:
    identity = False
else:
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if i != j and list1[i][j] != 0:
                identity = False
                break
            if i == j and list1[i][j] != 1:
                identity = False
                break            
if identity == True:
    print('identity matrix')        
else:
    print('not identity maatrix')

# Sum odf Diagonal elements

# list1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# sum = 0

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if i == j:
#             sum += list1[i][j]
# print(sum)