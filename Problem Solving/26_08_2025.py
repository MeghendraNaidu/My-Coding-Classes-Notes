# # Calculate the area of a square

# Area = int(input("Enter side of square: "))
# Area *= Area
# print("Area of square is:", Area)

# # Calculate the area of a rectangle.

# length = int(input("Enter length of Rectangle: "))
# breadth = int(input("Enter breadth of Rectangle: "))
# Area = length * breadth
# print("Area of Rectangle is:", Area)

# # Calculate the area of a triangle using base and height.

# Side = int(input("Enter side of Perimeter: "))
# Perimeter = 4 * Side
# print("Perimeter of square is:", Perimeter)

# # Calculate the perimeter of a rectangle. 
# length = int(input("Enter length of Rectangle: "))
# breadth = int(input("Enter breadth of Rectangle: "))
# Perimeter = 2 * (length + breadth)
# print("Perimeter of Rectangle is:", Perimeter)

# # Calculate the perimeter of a triangle. 
# Side1 = int(input("Enter F side of Triangle: "))
# Side2 = int(input("Enter S side of Triangle: "))
# Side3 = int(input("Enter T side of Triangle: "))
# Perimeter = Side1 + Side2 + Side3
# print("Perimeter of Triangle is:", Perimeter)

# # Break the total amount into denominations. 
# Amount = 3700

# One = Amount // 1000
# Remaining = Amount % 1000

# Five = Remaining // 500
# Remaining_Amount = Remaining % 500
# print(f"1000's:{One} - 500's:{Five} - Remaining:{Remaining_Amount}")

# # Convert Seconds into Hours, Minutes, Second
# Total_Seconds = 3672

# Hours = Total_Seconds // 3600
# Remaining_Seconds = Total_Seconds % 3600

# Minutes = Remaining_Seconds // 60
# Seconds = Remaining_Seconds % 60
# print(f"Hours: {Hours} - Minutes: {Minutes} - Seconds: {Seconds}")

# # Sum of MArks
# Maths_Marks = 85
# Physics_Marks = 90
# Chemistry_Marks = 88
# Total_Marks = Maths_Marks + Physics_Marks + Chemistry_Marks
# print("Total Marks:", Total_Marks)

# # Average Of Marks
# Maths_Marks = 85
# Physics_Marks = 90
# Chemistry_Marks = 88
# Total_Marks = Maths_Marks + Physics_Marks + Chemistry_Marks
# Average_Marks = Total_Marks / 3
# print("Average Marks:", Average_Marks)


# a, b = 0, 1
# count = 0
# for i in range(2, 11):
#     a, b = b, a + b
#     count += 1
# rows = [
#     [0],
#     [1, 4],
#     [2, 5, 7],
#     [3, 6, 8, 9]
# ]
# for r in rows:
#     for c in r:
#         print(a, end = " ")
#     print()


# for i in range(1, 5):
#     for j in range(i):
#         print(a, end = " ")
#         a, b = b, a + b
#         count += 1
#     print()

# def custom_fibonacci_pattern():
#     fib = [0,1]
#     for i in range(2, 15):
#         num = fib[-1] + fib[-2]
#         fib += [num]
         
#     rows = [
#         [0],
#         [1, 4],
#         [2, 5, 7],
#         [3, 6, 8, 9]
#     ]
     
#     for row in rows:
#         for i in row:
#             print(fib[i], end = " ")
#         print()
         
# print(custom_fibonacci_pattern())


# Input = (aabccca)
# Output = a2b1c3a1

