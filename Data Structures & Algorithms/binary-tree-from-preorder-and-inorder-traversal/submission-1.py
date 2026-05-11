# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: root, left, right
        #inorder: left, root, right
        # postorder: left, right, root
        
        # get the left tree and right tree form preorder and inorder
        # then build left and right recursively
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        #get the root index for inorder:
        # index = 0 
        # while index < len(inorder):
        #     if inorder[index] == root.val:
        #         break
        #     index += 1

        index = inorder.index(root.val)
        
        # index is the root node's index
        # left len is index + 1
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])

        return root
        
