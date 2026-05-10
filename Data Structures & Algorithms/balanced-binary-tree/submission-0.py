# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # for each node, left subtree and right subtree length different in max 1
        # so we need to get the left and right length
        # then compare the left and right length
        # is any of them has difference bigger than one the nwe nned to return False
        # otherwise, we keep going and check parent's node's if it is balanced by comapring max lengthe of right and left

        def dfs(node):
            if node is None:
                return True, 0
            
            left, left_len = dfs(node.left)
            right, right_len = dfs(node.right)

            if not left or not right:
                return False, max(left_len, right_len) + 1

            if abs(left_len - right_len) > 1:
                return False, max(left_len, right_len) + 1
            
            return True, max(left_len, right_len) + 1
        return dfs(root)[0]
        

        
        