# Transpose Of a Matrix
list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(list1)

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if i < j:
#             list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
            
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         print(list1[i][j], end = " ")
#     print()
    
# for i in range(n):
#     for j in range(i):
#         list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
            
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         print(list1[i][j], end = " ")
#     print()

# Recursion
# Base Condition => 

count = 0

def example():
    global count
    
    if count >= 3:
        return
    
    count += 1
    print(count)
    print("OG Bagundha?")
    example()
    
example()