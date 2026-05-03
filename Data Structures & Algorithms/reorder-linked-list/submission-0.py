# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # even: n/2-1, odd: n/2
        # both the second half starts at slow.next

        curr = slow.next
        slow.next = None
        # reverse secondhalf:
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        # now merge two lists, the prev is the head of second half
        left_half_curr = head
        while prev:
            tmp = prev.next # original curr.next
            prev.next = left_half_curr.next
            left_half_curr.next = prev
            prev, left_half_curr = tmp, prev.next


