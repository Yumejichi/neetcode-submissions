# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # divide to halves and merge them

        def mergeTwoList(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            
            if left:
                tail.next = left
            if right:
                tail.next = right
            
            return dummy.next

        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:

            merged = []
            # each time, merge two lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2= lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(mergeTwoList(l1, l2))
            lists = merged
        return lists[0]



            



        