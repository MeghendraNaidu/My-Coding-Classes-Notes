# 1. Check Even or Odd
# num = int(input("Enter a Number: "))
# if num % 2 == 0:
#     print("It is a Even")
# else:
#     print("It is a Odd")

# 2. Divisible by 5 but Not by 10
# num = int(input("Enter a Number: "))
# if num % 5 == 0 and num % 10 != 0:
#     print("Satisfy")
# else:
#     print("Not Satisify")

# 3. Biggest Among Two Numbers
# num1 = int(input("Enter First NUmber: "))
# num2 = int(input("Enter Second Number: "))
# print("Is Biggest") if num1 > num2 else print("Is Smallest")

# 4. Smallest Among Two Numbers
# num1 = int(input("Enter First NUmber: "))
# num2 = int(input("Enter Second Number: "))
# print("Is Smallest") if num1 < num2 else print("Is Biggest")

# 5. Divisible by 2, 3, and 6
# num = int(input("Enter a Number: "))
# print("Satisfy") if (num % 2 == 0 and num % 3 == 0) and (num % 6 == 0) else print("Not Satisfy")

# 6. Voting Eligibility
# Age = int(input("Enter Your Age: "))
# print("Eligible to Vote") if Age >= 18 else print("Not Eligible to Vote")

# 7. Student Pass/Fail Based on All Subjects >= 35
# Maths = float(input("Enter Maths Marks: "))
# Physics= float(input("Enter Physics Marks: "))
# Chemistry = float(input("Enter Chemistry Marks: "))
# print("Pass") if (Maths >= 35) and (Physics >= 35) and (Chemistry >= 35) else print("Fail")

# 8. Student Pass if Passed Any One Subject (>= 35)
# Maths = float(input("Enter Maths Marks: "))
# Physics= float(input("Enter Physics Marks: "))
# Chemistry = float(input("Enter Chemistry Marks: "))
# print("Pass") if (Maths >= 35) or (Physics >= 35) or (Chemistry >= 35) else print("Fail")

# 9. Student Pass if Passed Any Two Subjects
# Maths = float(input("Enter Maths Marks: "))
# Physics= float(input("Enter Physics Marks: "))
# Chemistry = float(input("Enter Chemistry Marks: "))
# if (Maths >= 35 and Physics >= 35) or (Chemistry >= 35):
#     print("Pass")
# elif (Maths >= 35 and Chemistry >= 35) or (Physics >= 35):
#     print("Pass")
# elif (Physics >= 35 and Chemistry >= 35) or (Maths >= 35):
#     print("Pass")
# else:
#     print("Fail")

# 10. Biggest Among Three Numbers
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# num3 = int(input("Enter Third Number: "))
# if num1 > num2 and num1 > num3:
#     print(num1, "Is Biggest")
# elif num2 > num1 and num2 > num3:
#     print(num2, "Is Biggest")
# else:
#     print(num3, "Is Biggest")

# 12. Perfect Square or Not
# num = int(input("Enter a Number: "))
# for i in range(1, int(num ** 0.5) + 1):
#     if i * i == num:
#         print(num, "It is a Perfect Number")
#         break
# else:
#     print(num, "It is Not a Perfect Number")

# 13. Cars Required for Members (Max 5 per car)
# members = int(input("Enter the Number of Members: "))
# cars = members // 5
# if members % 5 != 0:
#     cars += 1
# print("Cars Required:", cars)

# 14. Second Biggest Among Three Numbers
# A = 10
# B = 25
# C = 18

# second = A + B + C - max(A, B, C) - min(A, B, C)
# print(second)

# A = 10
# B = 25
# C = 18

# if (A > B and A < C) or (A > C and A < B):
#     second = A
# elif (B > A and B < C) or (B > C and B < A):
#     second = B
# else:
#     second = C
# print("Second Biggest:", second)

# 15. Leap Year or Not
Year = int(input("Enter a Year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "is a Leap Year")
else:
    print(Year, "is Not a Leap Year")