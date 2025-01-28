# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # odd_indices = list(filter(lambda elem: head.index(elem) % 2 != 0, head))
        # even_indices = list(filter(lambda elem: head.index(elem) % 2 == 0, head))

        if not head:
            return
        
        odd_indices, even_indices = [], []
        counter = 1
        while head.next:
            if counter % 2 == 0:
                even_indices.append(head.val)
            else:
                odd_indices.append(head.val)
            head = head.next
            counter += 1
        
        if counter % 2 == 0:
            even_indices.append(head.val)
        else:
            odd_indices.append(head.val)

        nodes = odd_indices + even_indices 
        node = ListNode(nodes[0])
        new_nodes, counter = [node], 1
        
        while counter < len(nodes):
            node = ListNode(nodes[counter])
            new_nodes[-1].next = node
            new_nodes.append(node)
            counter += 1
            
        return new_nodes[0]

            




solution = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = solution.oddEvenList(head)
while result:
    print(result.val, end=" ")
    result = result.next


# print(solution.oddEvenList([2,1,3,5,6,4,7])) #== [2,3,6,7,1,5,4]
# print(solution.oddEvenList([1,2,3,4,5])) #== [1,3,5,2,4]