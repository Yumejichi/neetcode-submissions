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

        # since it is binary search tree, we cmpare the root node with p and q
        if root is None:
            return None
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root