from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use minHeap
        minHeap = [] #val, index, node
        index = 0

        for i, head in enumerate(lists):
            if head:
                heappush(minHeap, (head.val, i, head))
        
        dummy = ListNode()
        prev = dummy
        while minHeap:
            val, index, node = heappop(minHeap)
            if node.next:
                heappush(minHeap, (node.next.val, index, node.next))
            prev.next = node
            prev = node
        return dummy.next
