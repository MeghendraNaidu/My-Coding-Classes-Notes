# Problem Solving

# Edges Cases
# Code Quality
# Try to Write every problem in Function
# Inbuilt Methods => 
# Interviews =>
# How to proceed with P.S questions in interviews.

list1 = [1, 2, 10, -11, 32, 62, 90]

def get_elem (input_list, index):
    if index < -1 * len(input_list) or index >= len(input_list):
        return 'Invalid Input'

    return input_list[index]
index = int(input('Enter a number'))
get_elem(index)

#Sum of elements, max and min in a given list


#Max
#1. Sorting
#2. Comparision

current_max = list1[0] # 0 cannot be taken initial value
current_min = list1[0]

for i in list1:
    sum += i
    
    if i > current_max:
        current_max = i

    if i < current_min:
        current_min = i


print(current_max)
    
