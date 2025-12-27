
# List collection of ordered and hetrogenous elemnets
list1 = [1, 2, 4, 5.5, 'str1', [1, 55, 72, [99]], 3+4j, [5,6]]
# print(list1)
# print(len(list1))
# print(list1[8])
# print(list1[5][2]) # For indentifying 72 We are accessing the 5th index list for indentifing the index 2 inside the list in list 2nd list
# print(list1[-3][-1][-1]) # For indentifing the 99 We are accessing the 5th index and inside 3rd index and finally mention the 99 index number
# print(list1[:: -1])
# print(list1[99 : 2212])
# list1[3] = 7.5
# print(list1)
# print(list1[3])


# Tuple
tup1 = (1, 2, 3, 5, 1, 7.6, 'String1')
# tup1[2] = 32 # Here item assignment is not possible
# print(tup1)
tup1 = (5, 6, 7, 8)


# String


# Rnage
# print(range(0 ,10))
# print(list(range(0, 10))) # For seeing the numbers we need to use the "list" before the range Ex :- list(range(0 ,10))
# print(list(range(10, 0, -2)))
# print(list(range(1, 50, 2))) # For Indentifying the Odd Numbers
# print(list(range(2, 50, 2))) # For Indentifying the Even Numbers
# print(list(range(13, 200, 13)))
# All multiple of 3 and 5 below 300
# print(list(range(15, 300, 15)))
# For printing Prime number in range it is not possible Because it dose not folow a specific patern or sequence.


# Dictionary => Dictionary is Ordered, Mutable, Value Duplication is possible
# Dictionary is a Ordered collection of key value pairs.
dict1 = {
    1 : 'Mahesh Babu',
    2 : '',
    3 : 'Dhanush',
    '4' : 'Rajendra Prasad',
    5 : 'Mohan Babu',
    6 : 'Surya',
    '7' : 'Surya',
    2 : 'Sradha kapoor'
}
print(dict1)
dict1[2] = 'AA'
print(dict1)

print(dict1[3])
print(dict1['4'])
