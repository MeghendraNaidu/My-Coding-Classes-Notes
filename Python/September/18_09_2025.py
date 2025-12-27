# Searching
# Linear Search 
# Binary Search

# Linear Search => 

# O(n) => Linear Time Complicity
# list1 = [10, -2, 45, 67, 81, 100, -200]
# search_elem = 200

# flag = True
# for i in range(0, len(list1)):
#     if list1[i] == search_elem:
#         print(i, "Element Found")
#         flag = False
#         break
    
# if flag == True:
#     print("Element Not Found")
    
def linear_search(input_list, search_elem):
    for i in range(0, len(input_list)):
        if input_list[i] == search_elem:
            return i
    
    return "Not Found"


# Binary Search => 

list1 = [10, -2, 45, 67, 81, 100, -200]
list1.sort()
print(list1)

# [-200, -2, 10, 45, 67, 81, 100]

n = len(list1)
low, high = 0, n - 1
search_elem = -200

flag = True
while low <= high:
    mid = (low + high) // 2
    
    if list1[mid] == search_elem:
        flag = False
        print(list1[mid], "Element Fount")
        break
    elif list1[mid] > search_elem:
        high = mid - 1
    else:
        low = mid + 1
if flag == True:
    print("Not Found")