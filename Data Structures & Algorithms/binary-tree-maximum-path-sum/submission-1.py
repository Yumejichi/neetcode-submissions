# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # left + right + node
        # or prev max

        maxSum = float("-inf")

        def dfs(node):
            nonlocal maxSum

            if node is None:
                return 0

            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            curr = node.val + left + right

            maxSum = max(maxSum, curr)
            return node.val + max(left, right)
        dfs(root)

        return maxSum