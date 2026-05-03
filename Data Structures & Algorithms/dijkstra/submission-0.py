class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for s, dest, w in edges:
            adj[s].append([dest, w])

        minHeap = [[0, src]]
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        # fill in missing nodes:
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1


        return shortest

        


