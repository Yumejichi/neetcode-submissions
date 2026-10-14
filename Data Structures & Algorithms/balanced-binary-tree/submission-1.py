# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return 0, True

            leftHeight, leftBalanced = helper(node.left)
            rightHeight, rightBalanced = helper(node.right)

            return max(leftHeight, rightHeight)+1, abs(rightHeight - leftHeight) <= 1 and leftBalanced and rightBalanced
        return helper(root)[1]

            
        