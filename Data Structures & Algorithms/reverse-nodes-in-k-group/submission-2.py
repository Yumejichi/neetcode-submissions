# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev_end = None
        dummy = ListNode()
        dummy.next = head

        # first check if there is k elems:
        while head:
            curr = head
            for _ in range(k - 1):
                if curr:
                    curr = curr.next

            if curr is None:
                break  # fewer than k nodes remain
            # we reverse this part
            # but first we set the head to current end's next
            next_head = curr.next
            curr.next = None
            # now we reverse the node from head to curr
            curr_head = head
            prev= None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt

            # now connect prev end to curr start (which is prev now)
            if prev_end:
                prev_end.next = prev
            else:
                dummy.next = prev
            prev_end = curr_head
            # 
            prev_end.next = next_head # incase there ie no k elems
            head = next_head
        return dummy.next
        
            
