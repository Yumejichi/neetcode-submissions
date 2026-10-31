from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for s,d,cost in flights:
            adjList[s].append((d, cost))
        
        minTotal = float("inf")
        visit = set()
        def dfs(node, total, count):
            nonlocal minTotal
            print(node, total)
            if total > minTotal:
                return

            if node == dst:
                minTotal = min(minTotal, total)
                return
            if count > k or node in visit:
                return
            visit.add(node)

            for neighbor,cost in adjList[node]:
                dfs(neighbor, total + cost,count+1)
            visit.remove(node)
        dfs(src, 0,0)
        return minTotal if minTotal != float("inf") else -1
                



