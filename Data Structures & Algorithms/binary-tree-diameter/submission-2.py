# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       # edges are node - 1
       # we can get the longest node len then minus 1
        maxLen = 0
        def helper(node):
            nonlocal maxLen
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            maxLen = max(maxLen, left+right)
            return max(left, right)+1
        helper(root)
        return maxLen

