# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        leftover = 0

        while l1 and l2:
            curr = ListNode()
            val = l1.val + l2.val + leftover
            leftover = 0
            if val >= 10:
                curr.val = val % 10
                leftover = val // 10
            else:
                curr.val = val
            prev.next = curr
            prev= curr
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr = ListNode()
            val = l1.val + leftover
            leftover = 0
            if val >= 10:
                curr.val = val % 10
                leftover = val // 10
            else:
                curr.val = val
            prev.next = curr
            prev= curr
            l1 = l1.next
        while l2:
            curr = ListNode()
            val = l2.val + leftover
            leftover = 0
            if val >= 10:
                curr.val = val % 10
                leftover = val // 10
            else:
                curr.val = val
            prev.next = curr
            prev= curr
            l2 = l2.next
        if leftover > 0:
            prev.next = ListNode(leftover)
        return dummy.next
                

