# Greatest of three numbers
num1, num2, num3 = 3, -5, 7
# if num1 > num2 and num1 > num3:
#     print(num1, "Is the Greaest Number")
# elif num2 > num3 and num2 > num1:
#     print(num2, "Is the Greaest Number")
# else:
#     print(num3, "Is the Greaest Number")
    
# if num2 < num1 > num3:
#     print(num1, "Is the Greaest Number")
# elif num1 < num2 > num3:
#     print(num2, "Is the Greaest Number")
# else:
#     print(num3, "Is the Greaest Number")

# Check if a year is a leap year
# def check_leap(year):
#     if year < 0:
#         return "Invalid Year"
#     # if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     #     return "Leap Year"
#     # # elif (year % 100 != 0 and year % 4 == 0):
#     # #     return "Leap Year"
#     # else:
#     #     return"Not a Leap Year"
    
#     return "Leap Year" if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else "Not a Leap Year"

# grade of a student
# def student_marks(marks):
#     if 90 < marks > 100:
#         return "Grade A"

# check if a triangle id valid triangle
# s1, s2, s3 = 3, 4, 5
# if (s1 + s2 > s3) and (s3 + s2 > s1) and (s1 + s3 > s2):
#     print("Valid Triangle")
# else:
#     print("Not a Valid Triangle")

# print even numbers using for and while loop
# n = 100
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)
# for i in range(2, n + 1, 2):
#     print(i)
    
# start = 0
# while start <= 100:
#     if start % 2 == 0:
#         print(start)
#     start += 1
    
start = 2
while start <= 100:
    print(start)
    start += 2