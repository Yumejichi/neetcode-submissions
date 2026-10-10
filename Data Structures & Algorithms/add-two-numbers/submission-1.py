# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        leftover = 0
        dummy = ListNode()
        prev = dummy

        while l1 and l2:
            total = l1.val + l2.val + leftover
            nodeVal = total % 10
            leftover = total // 10
            newNode = ListNode(nodeVal)
            prev.next = newNode
            prev = newNode
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + leftover
            nodeVal = total % 10
            leftover = total // 10
            newNode = ListNode(nodeVal)
            prev.next = newNode
            prev = newNode
            l1 = l1.next
        while l2:
            total = l2.val + leftover
            nodeVal = total % 10
            leftover = total // 10
            newNode = ListNode(nodeVal)
            prev.next = newNode
            prev = newNode    
            l2 = l2.next
        if leftover:
            newNode = ListNode(leftover)
            prev.next = newNode
        return dummy.next         

            

