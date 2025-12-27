# Class 1 roll 1
# Class 1 roll 2
# Class 1 roll 3
#  up to Class 1 roll 1 30

# i = 1
# while i < 31:
#     print(f" Class 1 Roll {i}")
#     i += 1

# count = 0
# for class_no in range(1, 11):
#     print(class_no)
#     for roll_no in range(1, 31):
#         count += 1
#         print("Class", class_no, "Roll", roll_no)
# print(count)

# for i in range(1, 13):
#     print(i)
#     for j in range(1, 21):
#         print(i, "X", j, "=", i * j)

# for class_no in range(1, 11):
#     if class_no % 3 == 0:
#         for roll_no in range(1, 31):
#             if roll_no % 7 == 0:
#                 print("Class", class_no, "Roll", roll_no)

class_no = 1
while class_no <= 10:
    roll_no = 1
    while roll_no <= 30:
        print("Class", class_no, "Roll", roll_no)
        roll_no += 1
    class_no += 1
