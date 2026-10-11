from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use minHeap
        minHeap = [] #val, node
        index = 0

        for head in lists:
            curr = head
            while curr:
                nxt = curr.next
                curr.next = None
                heappush(minHeap, (curr.val, index, curr))
                curr = nxt
                index += 1
        
        dummy = ListNode()
        prev = dummy
        while minHeap:
            curr = heappop(minHeap)[2]
            prev.next = curr
            prev = curr
        return dummy.next
