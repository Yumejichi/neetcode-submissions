# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        def dfs(node):
            if node is None:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        datas = data.split(",")
        index = 0
        def helper():
            nonlocal index
            if datas[index] == "N":
                index += 1
                return
            
            node = TreeNode(int(datas[index]))
            index += 1
            node.left = helper()
            node.right = helper()
            return node
        return helper()




