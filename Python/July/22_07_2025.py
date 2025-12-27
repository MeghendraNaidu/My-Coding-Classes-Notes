# Loop
# for

# While => If Condition Satisfy it will print the Output Else it break the Loop.


# i = 5
# while i < 3:
#     print("Hello Brother")
#     i -= 1

# n = int(input("Enter Number: "))
# i = 0
# while i < n:
#     print(i, end = " ")
#     i += 1

# n = int(input("Enter Table: "))
# i = 1
# while i < 21:
#     print(n, 'X', i, '=', n * i)
#     i += 1

# li = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num = int(input("Enter a number (1 to 7): "))
while num < 1 or num > 7:
    print("Invalid input! Please enter a number between 1 and 7.")
    num = int(input("Enter again: "))
print("Day is:", days[num - 1])
