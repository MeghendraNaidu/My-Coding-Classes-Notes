# Perrfect Number
# 6 => 1, 2, 3 => 6

# Check if the give number is a perfect Number
# Print all the perfect number in the given range

# Check if the number is perfect
num = int(input("Enter a Number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

def check_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return "is a Perfect Number"
    return "is not a Perfect Number"
# print(check_perfect(6))
    
    
# Print all perfect number in given range
# for i in range(1, 500):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if sum == i:
#         print(i, "is a perfect number")

# for i in range(1, 500):
#     if check_perfect(i) == "is a Perfect Number":
#         print(i, check_perfect(i))

# Find all prime numbers in a given number
# num = "2459"
# prime = [2, 3, 5, 7]
# for i in num:
#     if int(i) in prime:
#         print(i)
#     else:
#         pass

# Sum of nested lists
# list1 = [[1, 2, 3], [-5, 6, 7], [10, 12, 8]]
# sum = 0

# for i in list1:
#     for j in i:
#         sum += j
#
# print(sum)

# Reverse String
# str = "nani"
# rev = ""
# for i in str:
#     rev = i + rev
# print(rev)

# List Reverse
# list1 = [1, 2, 3, 4, 5]
# rev = []
# for i in list1:
#     rev.insert(0, i)
# print(rev)

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rev = []
# for i in list1:
#     for j in i:
#         rev.insert(0, j)

# print(rev) # And the reverse list want to store as a nested list
# nested_rev = []
# temp = []
# for i in rev:
#     temp.append(i)
#     if len(temp) == 3:
#         nested_rev.append(temp)
#         temp = [] # Reset temp for the next group
# print(nested_rev)

