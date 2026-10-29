"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            if node is None:
                return None
            if node not in oldToNew:
                new_node = Node(node.val)
                oldToNew[node] = new_node
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                oldToNew[node].neighbors.append(cloned_neighbor)

            return oldToNew[node]
        return dfs(node)
