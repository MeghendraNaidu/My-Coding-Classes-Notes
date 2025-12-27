# Prime Number = A number having 2 factors '1' and itself is called prime number
# A number divisible "1" and itself is called Prime Number
#2, 3, 5, 7, 11, 13, 17, 19, 23

# 24 => 1, 2, 3, 4, 6, 8, 12, 24 # This all are factors of "24"

# Method 1 # it is without functions

# num1 = int(input("Enter a Number: "))
# count = 0

# for i in range(1, num1 + 1):
#     if num1 % i == 0:
#         count += 1
        
# if count == 2:
#     print("Number is a Prime Number")
# else:
#     print("Number is Not a Prime Number")
    
# Method 2
# Definition => 
# num1 = int(input("Enter a Number: "))

# flag = True
# for i in range(2, num1):
#     if num1 % i == 0:
#         flag = False
#         print("It is Not a Prime Number")
#         break
# if flag == True:
    # print("It is a Prime Number")

# num1 = int(input("Enter a Number: "))
# if num1 <= 1:
#     print("It is Not a Prime Number")
# else:
#     flag = True
#     for i in range(2, num1):
#         if num1 % i == 0:
#             flag = False
#             print("It is Not a Prime Number")
#             break
#     if flag == True:
#         print("It is a Prime Number")

# Method 3
# def check_prime(num1):
#     if num1 <= 1:
#         return "Not a Prime"
    
#     for i in range(2, num1):
#         if num1 % i == 0:
#             return "Not a Prime"
        
#     return "Prime"


# Method 4
# 12 => 1, 2, 3, 4, 6, 12 # Here 12 half 6 in between both there is no factors
# 28 => 1, 2, 4, 7, 14, 28 # Here 28 half 14 in between both there is no factors
# 36 => 1, 2, 3, 4, 6, 9, 12, 18, 36 # Here 36 half 18 in between both there is no factors
# 7 => 1, 7 # Here 7 half 4 in between both there is no factors

# 12 => range 2 to 11
#    => range 6 to 11

def check_prime(num1):
    if num1 <= 1:
        return "Not a Prime"
    
    for i in range(2, num1 // 2 + 1):
        if num1 % i == 0:
            return "Not a Prime"
        
    return "Prime"
num1 = int(input("Enter a Number: "))
print(check_prime(num1))
