"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(cur):
            if cur is None:
                return None
            if cur in visited:
                return visited[cur]
            clone = Node(cur.val)
            visited[cur] = clone
            for neighbor in cur.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone


        return dfs(node)


