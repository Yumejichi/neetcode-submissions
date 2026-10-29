class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # use union find, we union the edge but if it returns false means it is already connected so we return that edge
        n = len(edges) # since we have an additional edge and if no cycle it should be have n-1 edges
        parents = list(range(n+1)) # start from 1, the 0 can be ignored
        rank = [1] * (n+1)

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False # already connected
            if rank[root_a] > rank[root_b]:
                parents[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                parents[root_a] = root_b
                rank[root_b] += rank[root_a]
            return True

        for u, v in edges:
            if not union(u,v):
                return [u,v]