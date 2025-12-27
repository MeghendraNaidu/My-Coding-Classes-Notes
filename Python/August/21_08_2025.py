list1 = [1, 2, 3, 2, 2, 4, 2]
# count = 0
# for i in list1:
#     if i == 2:
#         count += 1
# print(count)

# Count Inbuilt Function
# print(list1.count(2))

# Copy Inbuilt Function
# li = list1.copy() # If we don't use copy function here it will print the "list1" output for the "li" also.
#                   # If we don't need that output means we use copy function
# list1.pop()
# print(list1, li)

# Tuple Inbuilt Fuctions
# tup1.index()
# tup1.count()
# len(tup1)

# tup1 = (1, 2, 3, 4)
# print(tup1.index(1))

# String Inbuilt Functions
str1 = "meghendra"
# To get char to ascii - ord(char)
# To change ascii to char - chr(ascii value)
str1.upper() # To convert to uppercase
str1.lower() # To convert to lowercase
str1.islower() # To check whether the string is in lowercase or not
str1.isupper() # To check whether the string is in uppercase or not
str1.swapcase() # To swapcase change the string into upper to lower and lower to upper
len(str1) # To find the length of the String
str1.title() # To convert the first letter of each word to uppercase and the rest to lowercase
str1.capitalize() # To convert the first letter of the string to uppercase and the rest to lowercase
str1.strip() # To remove the spaces before and after the String
str1.rstrip() # To remove the space from ens of the String
str1.lstrip() # To remove the space from start of the String
str1.isalpha() # To check whether the string contains only alphabets or not

str1 = "i am a java trainer"
str1.replace("java", "python")
str1.replace("old value", "new value") # To replace a character or word in Sreing
