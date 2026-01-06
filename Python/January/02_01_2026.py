# # Regex or Regular Expresions


# #Regex is used to validate, extract, replace a specific patterns.

# pancardnum = "kdgfl7683d"


# r"[a-z]{5}[0-9]{4}[a-z]{1}"

# # Methods to check input with patterns

# # 1. match() it will check only first character
# # 2. search() it will check anywere in the word
# # 3. fullmatch()
# # 4. find()
# # 5. findall()
# # 6. sub()

# # to define the patterns using regex
# # r"pattern"
# # 1. every string should start with IND
# # eg: INDhello, INDwelcome, IND1234, INDok

# import re

# # re.match(pattern, input)
# x = re.match(r"IND", "IND123")
# if x:
#     print("It is a valid input")
# else:
#     print("Invalid input")
    
    
# # Sir Notes

# 123--->integer
# 123.25--->float
# "586ddfgjf"--->string


# "xyz29832213"
# "78979xyz7978"
# "dchdc54645"

#here we are having our own patterns for text.

#regex.--->

#integer,float,string,list,tuple,dictionary,regex.
import re

# ip1="SBIN1234"
# ip2="ICICI1234"
# ip3="AXIS1234"
# ip4="HDFC1234"
#regex
# match()--->it will checks the pattern in the given strin
# regex string or pattern
# op=re.match(r"ICICI",ip1)

# if op:
#     print("it is correct ifsc code")
# else:
#     print("it is incorrect ifsc code")


# ip1="ICICI1234"
# if re.match(r"SBIN",ip1):
#     print("it is sbi ifsc code")
# elif re.match(r"ICICI",ip1):
#     print("it is icici ifsc code")
# elif re.match(r"AXIS",ip1):
#     print("it is AXIS ifsc code")
# elif re.match(r"HDFC",ip1):
#     print("it is hdfc ifsc code")
# else:
#     print("invalid ifsc code")



#it can contains any alphabates but 4
#it can contains any numbers  but 5

#regex->
# [a-z]{4}
# [0-9]{5}

#starts with alphabates--> ^
#ends with number---> $

#user input should starts with any 4 alphabates and ends with any 5 numbers

# ip="CHARANTEJ25869"

# x=re.match(r"^[A-Z]{4,8}[0-9]{5,}$",ip)
# print(x)

# {m}-->length should be exactly m 
# {m,}--->length should be minimum m and maximum user wish 
# {m,n}--->length should be minimum m and maximum n .

# [j-q]
# [4-9]
#KOPLM3067Y
#KKK9996661
# ip_pan1="DEL903897T"

# op_pan=re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",ip_pan1)
# print(op_pan)
# if op_pan:
#     print("valid pan number")
# else:
#     print("invalid pan number")


# ip1="hello world"
# ip2="world hello welcome"
# ip3="hello hyderabad"

# x1=re.search(r"hello",ip1)
# print(x1)

# x2=re.search(r"hello",ip2)
# print(x2)

# x3=re.search(r"hello",ip3)
# print(x3)



#to validate input data with our customised patterns.

#match and search

#^,$,[],{}