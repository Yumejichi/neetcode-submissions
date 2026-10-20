from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [] # -distance, points

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heappush(maxHeap, (-dist, [x,y]))

            if len(maxHeap) > k:
                heappop(maxHeap)
        return [point for dist, point in maxHeap]