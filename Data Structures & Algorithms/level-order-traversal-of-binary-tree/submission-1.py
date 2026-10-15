# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        q = deque([root])

        while q:
            arr = []
            for _ in range(len(q)):
                curr = q.popleft()
                arr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(arr)
        return res
                
