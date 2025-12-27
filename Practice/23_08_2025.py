# rows = int(input("Enter rows: "))
# ch = 65
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(chr(ch), end = " ")
#         ch += 1
#         if ch > 90:
#             ch = 65
#     print()


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# lcm = max(num1, num2)
# while True:
#     if (lcm % num1 == 0) and (lcm % num2 == 0):
#         print(f'LCM of {num1} and {num2} is {lcm}')
#         break
#     lcm += 1


# def sort_by_length(arr):
#     return sorted(arr, key = len)
# strings = ["a", "ccc", "dddd", "bb"]
# result = sort_by_length(strings)
# print(result)


# a = ["a", "ccc", "dddd", "bb"]
# a.sort()
# print(a)


# print("A")
# print("BC")
# print("DEF")
# print("GHIJ")
# print("KLMNO")


# def store():
#     a = ["a", "ccc", "dddd", "bb"]
#     a.sort()
# store()

# Patterns

# Right-Angled Triangle

# rows = int(input("Enter rows: "))
# for i in range(1, rows + 1):
#         print("*" * i)
        
# Inverted Right-Angle Triangle

# rows = int(input("Enter rows: "))
# for i in range(rows, 0, -1):
#         print("*" * i)

# Pyramid

# rows = 5
# for i in range(1, rows+1):
#     print(" " * (rows-i) + "*" * (2*i-1))

# Diamond

# rows = 5
# # upper
# for i in range(1, rows+1):
#     print(" "*(rows-i) + "*"*(2*i-1))
# # lower
# for i in range(rows-1, 0, -1):
#     print(" "*(rows-i) + "*"*(2*i-1))

# Increasing Numbers

# rows = int(input("Enter rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()


# OOP's Concepts

# Class and Object
# Defining a class
# class Car:
#     # Properties (attributes)
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     # Method (behavior)
#     def drive(self):
#         print(f"{self.color} {self.brand} is driving...")

# # Creating objects
# car1 = Car("Tesla", "Red")
# car2 = Car("BMW", "Black")

# car1.drive()
# car2.drive()


# Secong largest Number

# numbers = [10, 25, 4, 98, 65, 98]

# # Remove duplicates
# unique_numbers = list(set(numbers))

# # Sort in descending order
# unique_numbers.sort(reverse=True)

# # Second largest
# print("Second largest number is:", unique_numbers[1])


# Second Smallest Number
# numbers = [10, 25, 4, 98, 65, 98]

# # Remove duplicates
# unique_numbers = list(set(numbers))

# # Sort in ascending order
# unique_numbers.sort()

# # Second smallest
# print("Second smallest number is:", unique_numbers[1])


def encode_string(s):
    if not s:
        return ""
    
    result = ""
    count = 1
    
    # Loop through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    # Append the last character and its count
    result += s[-1] + str(count)
    return result

# Example usage
input_str = "aabccca"
output_str = encode_string(input_str)
print(output_str)  # Output: a2b1c3a1


