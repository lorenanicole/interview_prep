class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return 
        
        old_node_to_new = {}

        # Instantiate a list of new new nodes, add to map of old to new nodes
        current = head
        while current:
            old_node_to_new[current] = Node(current.val)
            current = current.next

        # If it exists, set the new node's random to the new copy of the random 
        # node and the next node (using the map of old to new to retrieve the new 
        # node to set as next)
        current = head
        while current:
            new_node = old_node_to_new[current]

            if current.random:
                new_node.random = old_node_to_new[current.random]

            if current.next:
                new_node.next = old_node_to_new[current.next]
            
            current = current.next
        
        return old_node_to_new[head]

    def display(self, head):
        output = ""
        
        current = head
        while current:
            output += f"Node(id={id(self)}, val={current.val}, next={id(current.next)}, random={id(current.random)})"
            if current.next:
                output += "->"
            
            current = current.next
        
        print(output)


solution = Solution()

head = Node(x=1)
tail_node = Node(x=2)

head.next = tail_node
head.random = head
tail_node.random = head

solution.display(head)
n_head = solution.copyRandomList(head)
solution.display(n_head)