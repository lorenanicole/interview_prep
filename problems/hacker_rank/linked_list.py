# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
#     def __repr__(self):
#         return f'({self.data})'
    
# class LinkedList:
#     def __init__(self):
#         self.root = None
    
#     def add_to_start_list(self, node):
#         if not self.root:
#             self.root = node
#             return

#         else:
#             temp_root = self.root 
#             self.root = node
#             self.root.next = temp_root
    

#     def add_to_back_list(self, node):
#         temp = self.root
#         # import pdb; pdb.set_trace()
#         while temp:
#             if not temp.next:
#                 break
#             temp = temp.next
#         temp.next = node

#     def print_list(self):
#         temp = self.root # Start from the head of the list
#         output = ""
        
#         while temp:
#             output += temp.data # Print the data in the current node
#             if temp.next:
#                 output += "->"
#             # import pdb; pdb.set_trace()
#             temp = temp.next # Move to the next node
#         return output # Ensures the output is followed by a new line

#     def print_list_backwards(self):
#         values = []
#         temp = self.root
#         while temp:
#             values.append(temp.data)
#             temp = temp.next
#         size = len(values)
#         output = ""
#         for indx in range(len(values) - 1, -1, -1):
#             # import pdb; pdb.set_trace()
#             output += values[indx]
#             if indx != 0:
#                 output += "->"

#         return output

#     def delete_from_start(self):
#         if self.head is None:
#             return "The list is empty" # If the list is empty, return this string
#         self.head = self.head.next
    
#     def delete_from_end(self):
#         if self.root is None:
#             return "The list is empty" 
#         if self.root.next is None:
#             self.root = None  # If there's only one node, remove the head by making it None
#             return
#         temp = self.root
#         # import pdb; pdb.set_trace()
#         while temp.next.next:  # Otherwise, go to the second-last node
#             # import pdb; pdb.set_trace()
#             temp = temp.next
        
#         temp.next = None 
    
#     def insert_between_nodes(self, target_node_data, new_node):
#         temp = self.root
#         while temp:
#             if temp.data == target_node_data:
#                 new_node.next = temp.next
#                 temp.next = new_node
#                 return
#             else:
#                 temp = temp.next
# x.strftime("%m-%d-%Y"))
# datetime.timedelta(seconds=5)

# my_list = LinkedList()
# my_list.add_to_start_list(Node("world"))
# my_list.add_to_start_list(Node("hello"))
# my_list.add_to_back_list(Node("Lorena"))
# print(my_list.print_list())# == "hello->world")
# # print(my_list.print_list_backwards())# == "world->hello")
# my_list.delete_from_end()
# print(my_list.print_list())
# my_list.insert_between_nodes("world", Node("Eric"))
# print(my_list.print_list())

def reverse(llist):
    pass

class SinglyLinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = data if data else None

class SinglyLinkedList:
    def __init__(self):
        self.root = None

    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        
        temp_root = self.root 
        self.root = node
        self.root.next = temp_root
    
    def print_list(self):
        temp = self.root # Start from the head of the list
        output = ""
        
        while temp:
            output += str(temp.data) # Print the data in the current node
            if temp.next:
                output += "->"
            # import pdb; pdb.set_trace()
            temp = temp.next # Move to the next node
        return output # Ensures the output is followed by a new line
    
def reverse(head):
    temp = head
    output = []
    
    while temp:
        output.append(tempdata)
        temp = temp.next
    
    return output[::-1]
        


llist = SinglyLinkedList()
head = SinglyLinkedListNode(1)
llist.add_node(head)
llist.add_node(SinglyLinkedListNode(2))
llist.add_node(SinglyLinkedListNode(3))
print(llist.print_list())
print(reverse(llist.root))

# print(reverse())
