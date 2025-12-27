# Calculate the area of a square

# Area = int(input("Enter side of square: "))
# Area *= Area
# print("Area of square is:", Area)

# Calculate the area of a rectangle.

# length = int(input("Enter length of Rectangle: "))
# breadth = int(input("Enter breadth of Rectangle: "))
# Area = length * breadth
# print("Area of Rectangle is:", Area)

#Calculate the area of a triangle using base and height.

# Side = int(input("Enter side of Perimeter: "))
# Perimeter = 4 * Side
# print("Perimeter of square is:", Perimeter)

# Calculate the perimeter of a rectangle. 
# length = int(input("Enter length of Rectangle: "))
# breadth = int(input("Enter breadth of Rectangle: "))
# Perimeter = 2 * (length + breadth)
# print("Perimeter of Rectangle is:", Perimeter)

# Calculate the perimeter of a triangle. 
# Side1 = int(input("Enter F side of Triangle: "))
# Side2 = int(input("Enter S side of Triangle: "))
# Side3 = int(input("Enter T side of Triangle: "))
# Perimeter = Side1 + Side2 + Side3
# print("Perimeter of Triangle is:", Perimeter)

# Check_Triangle

def check_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not avalid  triangle"
    #type  of triangle
    if a == b== c:
        triangle_type = "equilateral"
    elif a==b or b==c or a==c:
        triangle_type="isosceles"
    else:
        triangle_type="scalene"
    # check for right angled traingle
    sides = sorted([a,b,c])
    if sides[0]**2 + sides[1]**2 ==sides[2]**2:
        triangle_type+= " and right_angled triangle"
    return triangle_type


a=float(input("enter side 1:"))
b=float(input("enter side 2:"))
c=float(input("enter side 3:"))
print(check_triangle(a,b,c))