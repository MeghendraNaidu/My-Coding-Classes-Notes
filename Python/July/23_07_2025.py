# s = {10, 20, 30, 10, 90}
# for n in s:
#     print(n)

# dict1 = { 1: "Ram", 2 : "Venkat", 3 : "Sai" }
# for i in dict1:
#     print(i) # For printing Values we use "dict1.values" or "print(d[i])"

# str = "String"
# count = 0 # For counting a Character without using function
# for i in str: # For reverse String we use "str[::-1]"
#     count += 1
#     print(count)
#     print(i, end ="")

# str = "Hello Python"
# count = 0
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# for i in str:
#     if i in vowels:
#         count += 1
#         print(count)
        # print(i, end = "")

# lis = [22, 45, 67, 2, 56, 99, 347, 113, 23, 234]
# even_count = 0
# odd_count = 0
# for i in lis:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(even_count)
# print(odd_count)

str = input("Enter a Character:")
# small = 0
# for i in str:
if 'A' <= str <= 'Z':
    print("It is a Upper Case")
    str = str.lower()
    print(str)
else:
    print("It is Already a Lower Case")
    