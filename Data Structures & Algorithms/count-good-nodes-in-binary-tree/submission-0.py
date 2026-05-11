# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def dfs(node, max_till_now):
            nonlocal res
            if node is None:
                return
            if node.val >= max_till_now:
                res += 1
                max_till_now = node.val
            
            dfs(node.left, max_till_now)
            dfs(node.right, max_till_now)

        dfs(root, float("-inf"))
        return res