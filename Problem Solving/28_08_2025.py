# n = input("Enter your Character: ")
# d = {} # It is used for Printing values in dictionary format
# if 'A' <= n <= 'Z':
#     print("It is a Upper Case")
#     res = chr(ord(n) + 32)
#     print(f'{n} => {res}')
# else:
#     print('It is a Lower Case')
#     asci = ord(n)
#     d[n] = asci
#     print(d)
#     # print(f'{n} : {asci}')

# Extract Special Characters
# n = "NaniT2@%@.com"
# for i in n:
#     if not (('A' <= i <= 'Z') or ('a' <= i <= 'z') or (48 <= ord(i) <= 57)):
#         print(i)

# Printing Telugu Characters
n = 3077
while n <= 3183:
    print(chr(n), end=" ")
    n += 1

