# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first we get the middel elem:
        slow, fast = head, head
        while fast.next and fast.next.next: # stops one before the end, slow stops in one before mid
            slow = slow.next
            fast = fast.next.next
        # the slow point is current middle
        # we reverse the second half of the linkedlist
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        # we get the reversed second half head as prev
        # Now we merge them:
        first = head
        while first and second:
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            first, second = first_nxt, second_nxt
