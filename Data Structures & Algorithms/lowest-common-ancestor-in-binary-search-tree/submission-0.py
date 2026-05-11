# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the common ancestor can be grouped into:
        # p,q is on same side of a root or itself and another childern -> the p or q which ever is parent
        # p q is in left and right of a node -> the root node

        def dfs(node, p, q):
            if node is None:
                return None
            
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left == p and right == q or (left == q and right == p):
                return node
            if left is None:
                return right
            if right is None:
                return left
            
        return dfs(root, p, q)