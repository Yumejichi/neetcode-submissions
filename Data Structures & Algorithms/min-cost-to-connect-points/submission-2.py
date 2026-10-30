class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.parents[root_b] = self.parents[root_a]
            self.rank[root_a] += self.rank[root_b]
        else:
            self.parents[root_a] = self.parents[root_b]
            self.rank[root_b] += self.rank[root_a]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        n = len(points)
        dsu = DSU(n)

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist,i,j))
        edges.sort()
        count = 0
        res = 0
        for dist, u, v in edges:
            if dsu.union(u,v):
                count += 1
                res += dist
                if count == n-1:
                    break
        return res


        