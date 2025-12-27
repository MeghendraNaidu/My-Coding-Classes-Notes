# prime numbers from 1 to 100 and count
# for i in range(1, 101):
#     if i > 1:
#         for j in range(2, i + 1):
#             if i % j != 0:
#                 print(i, end = " ")
#                 break
#             else:
#                 pass

# print all armstrong number from 1 to 500.
# m = 1
# n = 500
# for i in range(m, n + 1):
#     num = i
#     sum = 0
#     original_num = num
#     n = len(str(original_num))
#     while original_num > 0:
#         digit = original_num % 10
#         sum += digit ** n
#         original_num //= 10
#     if sum == num:
#         print(i)

# print all even number from 1 to 100 using "continue"
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     else:
#         print(i, end = " ")
        
# def even_num(m, n):
#     for i in range(m, n):
#         if i % 2 != 0:
#             continue
#         else:
#             print(i, end = " ")
# even_num(1, 101)

