# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level, only add the most right side of the node,
        # use q to traverse each level and add the last one
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if i == len_q-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
                