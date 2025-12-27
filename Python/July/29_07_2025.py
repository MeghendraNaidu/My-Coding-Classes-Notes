# Jump Statements - Break, Continue and Pass

# Break => Once the break hits the loop and the loop will stop immediatlly


# for i in range(1, 100):
#     # print(i)
#     if i == 50:
#         break
#     print(i)

# Continue => 

# for i in range(1, 25):
#     print(i)
#     if i == 8:
#         continue
#     print(i)
#     print(i)

# for i in range(1, 32):
#     if i < i * (-1):
#         continue
#     print(i ** 2)

# Break and Continue in Nested Loop

# for class_no in range(1, 11):
#     for roll_no in range(1, 31):
#         if roll_no == 5:
#             break
#         print(class_no, roll_no)

# for class_no in range(1, 11):
#     for roll_no in range(1, 31):
#         if roll_no == 5:
#             continue
#         print(class_no, roll_no)

# for class_no in range(1, 11):
#     for roll_no in range(1, 31):
#         if class_no > 5 or roll_no < 16:
#             print(class_no, roll_no)

# for class_no in range(1, 11):
#     for roll_no in range(1, 31):
#         if class_no > 5 or roll_no < 16:
#             break
#         print(class_no, roll_no)
    
# Pass =>

num1 = 10
if num1 % 2 == 0:
    pass
else:
    print("Odd Number")