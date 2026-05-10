# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # function for reverse the node:
        def reverseLinkedList(node):
            dummy = ListNode()
            # move from current node and put it infront of the new list
            while node:
                tmp = node.next
                node.next = dummy.next
                dummy.next = node
                node = tmp
            
            return dummy.next
        
        dummy = ListNode()
        dummy.next = head
        pre_tail = dummy
        while pre_tail:
            # check if ther is k counts:
            curr = pre_tail
            for _ in range(k):
                curr = curr.next
                if curr == None:
                    # just return the current list since no reverse needed
                    return dummy.next
            
            # reverse the linkedlist
            # before reverse, rememenber current tail befre reverse it
            group_head = pre_tail.next
            nxt_group_head = curr.next
            curr.next = None # disconnect current part first
            pre_tail.next = reverseLinkedList(group_head)
            group_head.next = nxt_group_head
            pre_tail = group_head

        return dummy.next



        


