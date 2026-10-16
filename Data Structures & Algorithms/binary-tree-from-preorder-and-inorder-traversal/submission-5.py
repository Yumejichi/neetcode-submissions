# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track the current root element in preorder sequence
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the subtree
            if in_left > in_right:
                return None
            
            # Select the current preorder element as root
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Split the inorder list around the root index
            mid = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)
            