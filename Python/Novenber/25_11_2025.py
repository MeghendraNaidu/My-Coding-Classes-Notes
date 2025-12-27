# Linked List
class Node:
     
     def __init__(self, data):
          self.data = data
          self.next = None

# head is nothing but n1
head = Node(5) # here n1 is head

head1 = Node(-4)
head.next = head1

n3 = Node(10)
head1.next = n3

# Display of Linked List

def print_11(head):
    
    if head == None:
        return
    temp = head
    
    while temp != None:
        print(temp.data)
        temp = temp.next
        
print_11(head1)

# Insert a Node at the start
# def add_node_start(head, new_node_data):
    
    
# Sir Notes

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


#head is nothing but n1
head1 = Node(5)
n2 = Node(-4)
head1.next = n2
n3 = Node(10)
n2.next = n3




#Display of LL



def print_ll (head):

    if head == None:
        return
    
    temp = head

    while temp != None:
        print(temp.data)
        temp = temp.next


print_ll(head1)



#Insert a node at the start
def add_node_start (head, new_node_data):


    new_node = Node(new_node_data)
    new_node.next = head
    head = new_node
    return head


head1 = add_node_start(head1, 25)
    
print_ll(head1)



def add_node_last(head, new_node_data):

    if head == None:
        new_node = Node(new_node_data)
        head = new_node
        return head


    temp = head
    while temp.next != None:
        temp = temp.next

    
    new_node = Node(new_node_data)
    temp.next = new_node
    return head





def delete (head, del_data):

    if head == None:
        return 
    
    if head.data == del_data:
        head = head.next
        return
    

    temp = head
    prev = None
    while temp != None:

        if temp.data == del_data:
            prev.next = temp.next
            return 

        prev = temp
        temp = temp.next
        

delete(head1, -4)
print_ll(head1)




#Reverse a linked list