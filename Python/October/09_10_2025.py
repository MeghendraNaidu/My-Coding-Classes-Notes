# *
# * * *
# * * * * *
# * * * * * * *

n = 5
#1st row => i = 0 => stars = 1
#2st row => i = 1 => stars = 3
#3st row => i = 2 => stars = 5
#4st row => i = 3 => stars = 7

#row + i = starts
#i + 1 + i => 2i + 1


for i in range(n):
    for j in range(2 * i + 1):
        print('*', end=' ')
    print()



#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


#last row = 0
#n-2 => 2
#n - 3 => 4
#n - 4 => 6

#



for i in range(n):
    one_visited = False
    start = i + 1
    for sp in range(2 * (n-i-1)):
        print(' ', end='')

    for j in range(2 * i + 1):
        print(start, end=' ')
        if start == 1:
            one_visited = True
        
        if one_visited == False:
            start -= 1
        else:
            start += 1
    print()



#
# print(chr(65)) # 66 # chr(66)
# print(chr(61))


# print(ord('a'))




for i in range(7):
    start = 65
    for j in range(7):
        print(chr(start), end=' ')
        start += 1
    print()


#Traingle => right angle traingle
#even rows => print numbers in ascending order
#odd rows => descending order
#Exclude prime number

#1
#1 2
#3 2 1
#1 2 3 4


#1
#2 3
#6 5 4
#7 8 9 10


start = 65
temp = ''
for i in range(7):
    temp += chr(start)
    start += 1

print(temp)

for i in range(7):
    print(temp)