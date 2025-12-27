# n = 23579812
# for i in str(n):
#     if i in "2357":
#         print(i)

# str1 = "venkata_narayana_battula"
# str1 = str1.title()
# str2 = ""
# for i in str1:
#     if i == "_":
#         continue
#     else:
#         str2 += i
# print(str2)

str1 = "World Health Organization"
str2 = ""
for i in str1:
    if i == " ":
        str2 += "."
    else:
        if i.title() == i[0]:
            str2 += i
print(str2)

# num = 14
# fact = 1
# while num < 0:
#     digit = num % 10
#     for i in range(1, digit):
#         fact *= digit
#     print(fact)
