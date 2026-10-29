class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [node for node in range(n)]
        rank = [1] * n

        def find(node):
            if parents[node] != node:
                return find(parents[node])
            return node

        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False # we don't union it since they are already connected

            if rank[root_a] >= rank[root_b]:
                parents[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                parents[root_a] = root_b
                rank[root_b] += rank[root_a]
            return True
        roots = n
        for u, v in edges:
            if not union(u,v):
                # we already connected, worng if still have an edge connect these two nodes
                return False
            roots -= 1

        return roots == 1

            
