class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num = n

        parents = list(range(n))
        rank = [1] * n

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            if rank[root_a] > rank[root_b]:
                parents[root_b] = root_a
                rank[root_a] += root_b
            else:
                parents[root_a] = root_b
                rank[root_b] += rank[root_a]
            return True
        
        for u, v in edges:
            if union(u,v):
                num -= 1
        return num