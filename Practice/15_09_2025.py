# Reverse a String
# str1 = "Python"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print(str2)

# str1 = list("Python")
# low = 0
# high = len(str1) - 1
# while low < high:
#     str1[low], str1[high] = str1[high], str1[low]
#     low += 1
#     high -= 1
# print(str(str1))

# str1 = list("Python")
# low = 0
# high = len(str1) - 1
# while low < high:
#     str1[low], str1[high] = str1[high], str1[low]
#     low += 1
#     high -= 1
# str1 = "".join(str1)
# print(str1)

# sum of digits
# list1 = [123, 456, 78, 91, 56]
# list2 = []
# for i in list1:
#     n = i
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n //= 10
#     list2.append(sum)
# print(list2)

# num = 471
# num1 = []
# while num > 0:
#     digit = num % 10
#     num //= 10
#     # num1.append(digit)
#     num1.insert(0, digit)
# # print(num1)
# current_max = num1[0]
# for i in num1:
#     if i > current_max:
#         current_max = i
# print(current_max)
    
list1 = [123, 456, 78, 91, 56]
list2 = []

for num in list1:
    num1 = num
    max_digit = 0
    while num1 > 0:
        digit = num1 % 10
        if digit > max_digit:
            max_digit = digit
        num1 //= 10
    list2.append(max_digit)
print(list2)