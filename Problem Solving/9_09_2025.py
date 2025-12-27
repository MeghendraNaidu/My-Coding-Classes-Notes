# Remove spaces from a string
# str1 = "he llo wor ld"

# def remove_space(str1):
#     s = ""
#     for i in str1:
#         if i==chr(32):
#             continue
#         else:
#             s+=i 
#     return s

# print(remove_space("he llo wor ld"))

# Reverse a String
# def reverse_string(str1):
#     rev_str = ""
#     for i in str1:
#         rev_str = i + rev_str
#     return rev_str

# s = input("Enter a String: ")
# print(reverse_string(s))

# conver snake case to camel case
# def convert(str1):
#     str1 = str1.title()
#     str2 = ""
#     for i in str1:
#         if i == "_":
#             pass
#         elif i == str1[0]:
#             str2 += i.lower()
#         else:
#             str2 += i
#     return str2
# s = input("Enter a String: ")
# print(convert(s))

# convert snake case to pascal case
def convert(str1):
    str1 = str1.title()
    str2 = ""
    for i in str1:
        if i == " ":
            pass
        else:
            str2 += i
    return str2
s = input("Enter a String: ")
print(convert(s))
    