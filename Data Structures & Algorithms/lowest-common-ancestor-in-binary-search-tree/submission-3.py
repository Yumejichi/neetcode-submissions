# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if they are in different side, current node is the lca
        # if on same side, either of them is the lca
        # since this is BST
        # if root == p or q, we return it
        # if p < root < q or q < root < p: return root
        if not root:
            return

        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
