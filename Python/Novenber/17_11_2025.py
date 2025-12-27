# Stack =>LIFO(last in first out), FILO(first in last out)

# list => []
# [2, 3, 4, 5, 8, 10]

# push it is used to add values in last position, 
# pop it is used to delete values which is in last position, 
# peek() it is used to show the value which is in last position, 
# size it is used to shoe length of stack, 
# is_empty() is used to tell that the stack is empty or not


# class Stack:
    
#     def __init__(self):
#         self.inner_list = []
#         print("Stack is Created")
    
#     def push(self, elem):
#         self.inner_list.append(elem)
    
#     def size(self):
#         return len(self.inner_list)
    
#     def is_empty(self):
#         return len(self.inner_list) == 0
        
#     def peek(self):
#         if self.is_empty():
#             raise Exception("No elements in the stack")
#         # return self.inner_list[len(self.inner) - 1]
#         last_ind = len(self.inner_list) - 1
#         return self.inner_list[last_ind]
    
#     def pop(self):
#         if self.is_empty():
#             raise Exception("No elements in the stack")
#         return self.inner_list.pop()
    
# s1 = Stack()

# s1.push(5)
# s1.push("5")
# s1.push(8)
# s1.push("No elements in the stack")
# s1.push(555)
# s1.push(0)

# print(s1.peek())
# print(s1.size())
# print(s1.is_empty())
# print(s1.pop())
# print(s1.size())
    

# Queue => 