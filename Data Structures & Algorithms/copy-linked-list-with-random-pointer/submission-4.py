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
        oldToNew = {None: None}

        if not head:
            return None

        curr = head

        while curr:
            if curr.next and curr.next not in oldToNew:
                oldToNew[curr.next] = Node(curr.next.val)
            if curr.random and curr.random not in oldToNew:
                oldToNew[curr.random] = Node(curr.random.val)
            if curr in oldToNew and oldToNew[curr] is not None:
                oldToNew[curr].val = curr.val
                oldToNew[curr].next = oldToNew[curr.next]
                oldToNew[curr].random = oldToNew[curr.random]
            else:
                oldToNew[curr] = Node(curr.val, oldToNew[curr.next], oldToNew[curr.random])
            curr = curr.next
        return oldToNew[head]

        

            
