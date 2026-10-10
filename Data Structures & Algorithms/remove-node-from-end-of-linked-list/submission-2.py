# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
        #          .   f.   
        #          s         f
        #               s         f
        #                     s        f
        #.                        s          f
        # we first move fast pointer k times
        # then use a slow one from head and move together with fast one until fast.next is None
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n):
            if fast.next:
                fast = fast.next
            else:
                return head # since we don't have that node. no need to remove
        # 1 -> 2, k =1
          
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # we remove the node after slow
        slow.next = slow.next.next
        return dummy.next
        