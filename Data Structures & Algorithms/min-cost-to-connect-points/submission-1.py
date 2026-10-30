from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for index, (x1,y1) in enumerate(points):
            for x2,y2 in points[index+1:]:
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[(x1,y1)].append((x2,y2,dist))
                adjList[(x2,y2)].append((x1,y1,dist))
                
        heap = [(0, points[0])]
        count = 0
        visited = set()
        total = 0
        while heap and count < len(points):
            dist, [x, y] = heappop(heap)
            if (x,y) in visited:
                continue
            total += dist
            visited.add((x,y))
            for a,b,dist in adjList[(x,y)]:
                if (a,b) not in visited:
                    heappush(heap, (dist, [a,b]))
            
            count += 1
        return total





