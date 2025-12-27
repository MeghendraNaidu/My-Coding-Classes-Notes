# Can you wrtie bubble sort for decending order

# list1 = [-2, -200, 10, 45, 67, 81, 100]

# for i in range(0, len(list1) - 1):
#     flag = True
#     for j in range(0, len(list1) - 1 - i):
#         if list1[j] < list1[j + 1]:
#             flag = False
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     if flag == True:
#         break
#     print(list1)

# Use bubble sort to sort strings => How will you get the output

# str1 = "vfskbsdkjfdshbdskjdbvhj"
# str1 = list(str1)
# for i in range(0, len(str1) -1):
#     flag = True
#     for j in range(0, len(str1) - 1 - i):
#         if str1[j] > str1[j + 1]:
#             flag = False
#             str1[j], str1[j + 1] = str1[j + 1], str1[j] 
#     if flag == True:
#         break
# str1 = "".join(str1)
# print(str1)


# Use bubble sort to sort strings based on their lengths. That is strings with highest length should go to last
# Can you sort nested lists based on the first element of each nested list.
 
# list1 = [-2, -200, [10, 45, 67], 81, 100]

def bubble_sort_list(lst):
    # bubble sort for a normal list
    for i in range(len(lst) - 1):
        flag = True
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False
        if flag:  # already sorted
            break
    return lst

nested_list = [[3, 2, 1], [5, 4, 6], [9, 7, 8]]

# print(bubble_sort_list(nested_list))

# sort each inner list using bubble sort
for i in range(len(nested_list)):
    nested_list[i] = bubble_sort_list(nested_list[i])

print(nested_list)
