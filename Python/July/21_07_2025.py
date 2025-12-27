# Loops => 
# Advantages of Loops => file size or space, time efficiency, maintainability, 
# Loops => for, while

# Iterable => list, Tuple, String, Dictionary, Set, Range
# for i in range(0, 11):
#     print('Hi')
#     print('Hello')
#     print('Good Morning')
#     print(i)

# print('Whole NUmbers')
# for i in range(0, 11):
#     print(i)
    
# print("Even")
# for i in range(0, 11, 2):
#     print(i)
    
# print("Odd")
# for i in range(1, 11, 2):
#     print(i)
    
# for i in range(0, 11):
#     if i % 2 == 0:
#         print(i, 'Even')
#     else:
#         print(i, 'Odd')

# 40 to 49 and 70 to 79
# for i in range(1, 100):
#     if i >= 40 and i < 50:
#         print(i)
#     elif i >= 70 and i < 80:
#         print(i)

# for i in range(1, 100):
#     if (40 <= i <= 49):
#         print(i)
#     elif (70 <= i <= 79):
#         print(i)

# for i in range(1, 100):
#     if (40 <= i <= 49) or (70 <= i <= 79):
#         print(i)

# for i in range(1, 341):
#     if i % 17 == 0:
for t in range(1, 21):
    print(17, "X", t, "=", 17 * t)
        
# n = int(input("Enter Table: "))
# for i in range(1, 21):
#     print(n, "X", i, "=", n*i)