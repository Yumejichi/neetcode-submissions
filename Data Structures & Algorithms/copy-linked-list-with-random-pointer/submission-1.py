"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        originalToNewMap = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            originalToNewMap[curr] = new_node
            curr= curr.next

        new_head = originalToNewMap[head]

        curr = head
        while curr:
            new_node = originalToNewMap[curr]
            if curr.next:
                new_node.next = originalToNewMap[curr.next]
            if curr.random:
                new_node.random = originalToNewMap[curr.random]
            curr = curr.next

        return new_head

