# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def helper(node, maxNum):
            if not node:
                return
            nonlocal count
            if node.val >= maxNum:
                count += 1
            
            helper(node.left, max(maxNum, node.val))
            helper(node.right, max(maxNum, node.val))
        helper(root, float("-inf"))
        return count
            
