# factorial of a Number
# num1 = 1
# n = 15
# fact = 1
# while num1 <= n:
#     fact *= num1
#     num1 += 1
# print(fact)

# def cal_fact(n):
#     if n < 0:
#         return "Fact is Not Possible"
#     num1 = 1
#     fact = 1
#     while num1 <= n:
#         fact *= num1
#         num1 += 1
        
#     return fact

# n = int(input("Enter the Number: "))
# print(cal_fact(n))
    
# print all Numbers from 1 to 100 that are divisble by 3 and 5 using a for loop.

# Implement a menu-driven program where the user can choose to;
# 1. find the square of a number
# 2. find the cube of a number
# 3. exit

# Implement a basic login system where the user has three attempts to enter the correct password using a loop.
db_username = "meghendra"
db_password = "12345"

# input_username = input("Enter Username: ")
# input_password = input("Enter Password: ")

# if (input_username == db_username) and (input_password == db_password):
#     print("Login Done")
# else:
#     print("Login Failed")
    
# remaining_attempts = 3

# while remaining_attempts > 0:
#     input_username = input("Enter Username: ")
#     input_password = input("Enter Password: ")

#     if (input_username == db_username) and (input_password == db_password):
#         print("Login Done")
#         break
#     else:
#         print("Login Failed")
    
#     remaining_attempts -= 1
    
#     print("Please Enter The Correct Username and Password")

num1 = 12534
# count = 5
# sum = 15

# using Strings
# print(len(str(num1)))
# str1 = str(num1) # 12534
# sum = 0
# for i in str1:
#     sum += int(i)
# print(sum)

# print(int(str(num1)[:: -1]))

# Using Number System Properties
# 356 % 10 => 6
# 459 % 10 => 9
# 321 % 10 => 1
# 50 % 10 => 0
# 5 % 10 => 5

# 2456
# Rem = 6, Que = 245
# Rem = 5, Que = 24
# Rem = 4, Que  = 2
# Rem = 2, Que = 0

num1 = 2456
count = 0
sum = 0

while num1 > 0:
    rem = num1 % 10
    print(rem)
    # que = num1 // 10
    # num1 = que
    num1 //= 10 
    count += 1
    sum += rem
    
print(sum)
print(count)
    



# This from Naga Raju
# write a program to calculate the  Factorail of a number using a while loop?
# num1=int(input("Enter the Number=  "))
# fact=1
# while num1>0:
#     fact= fact*num1
#     num1=num1-1 
#     print(fact)

# # print all number from 1 to 100 that are divisible y 3 and 5 suing a for loop?
# for i in range(1,101)  :
#     if i % 3==0 and i% 5==0:
#         print(i) 

# Implement a menu-driven program where the user can choose to:
# 1. Find the sqare of a number.
# 2. find the cude of a number
# 3. Exit
# while True:
#     print('1. square 2. cube 3.add 4.sub 5.mul 6.div')  
#     input_op = input ('choose an operator= ').lower()

#     if input_op == '1' or input_op == 'square':
#         input_num = float (input('Enter the Number to Square= '))  
#         print(input_num ** 2) 

#     elif input_op == '2' or input_op == 'cube':
#         input_num = float (input('Enter the Number to cube= '))  
#         print(input_num ** 3) 

#     elif input_op == '3' or input_op == 'add':
#         num1 = float (input('Enter the Number= '))  
#         num2 = float (input('Enter the Number= '))  
#         print(num1 + num2)

#     elif input_op == '4' or input_op == 'sub':
#         num1 = float (input('Enter the Number= '))  
#         num2 = float (input('Enter the Number= '))  
#         print(num1 - num2)   

#     elif input_op == '5' or input_op == 'mul':
#         num1 = float (input('Enter the Number= '))  
#         num2 = float (input('Enter the Number= '))  
#         print(num1 * num2) 

#     elif input_op == '6' or input_op == 'div':
    
#         num1 = float (input('Enter the Number= '))  
#         num2 = float (input('Enter the Number= ')) 
#         if num2  !=0:
#             print(num1 / num2)  
#         else:
#             print(' Zero divisable ')  

#     else:   
#         print ('Invalid')