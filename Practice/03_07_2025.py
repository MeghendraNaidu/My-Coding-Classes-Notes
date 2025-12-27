
# 1. Given the total seconds, compute and print equivalent hours, minutes, and seconds using arithmetic operations.

total_seconds = int(input("Enter the Seconds ="))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, "Hours", minutes, "Minutes", seconds, "Seconds")


# 2. Assign the price and quantity of two products. Calculate the total cost including 18% tax. Print a detailed bill.

price_1 = int(input("Enter Product One Price ="))
quantity_1 = int(input("Enter No of Quantity One ="))

price_2 = int(input("Enter Product Two Price ="))
quantity_2 = int(input("Enter No Of Quantity Two ="))

cost_1 = price_1 * quantity_1
cost_2 = price_2 * quantity_2

sub_total = cost_1 + cost_2

tax = sub_total * 0.18

total_cost = sub_total + tax


print("Price 1 * Quantity 1 :-", cost_1)
print("Price 2 * Quantity 2 :-", cost_2)
print("Sub Total :-", sub_total)
print("Tax(18%) :-", tax)
print("Amount To Pay :-", total_cost)

# print(total_cost)


# 3. Compute the perimeter and area of a circle given a radius. Use the value of π from the math module.

import math

radius = int(input("Enter the Radius ="))

perimeter = 2 * math.pi * radius
Area = math.pi * radius ** 2

print(perimeter)
print(Area)


# 4. Given a temperature in Celsius, convert it to Fahrenheit using the formula and print both values.(F = C × 9/5 + 32)

Celsius = int(input("Enter the Celsius ="))
Fahrenheit = Celsius * 9 / 5 +32

print("Celsius :-", Celsius)
print("Fahrenheit :-", Fahrenheit)


# 5. What is a compiled language? What is an interpreted language?Explain pros and cons of each. How hybrid languages bring in advantages of both.

