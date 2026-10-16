# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, maxNum, minNum):
            if not node:
                return True
            if minNum < node.val < maxNum:
                left = helper(node.left, node.val, minNum)
                right = helper(node.right, maxNum, node.val)
                return left and right
            return False
        return helper(root, float("inf"), float("-inf"))