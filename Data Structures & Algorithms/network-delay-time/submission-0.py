from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimes = [float("inf")] * (n+1)
        adjList = defaultdict(list)
        for u,v,time in times:
            adjList[u].append((v,time))


        minTimes[k] = 0
        heap = [(0,k)] # time, node

        while heap:
            curr_total, node = heappop(heap)
            for neighbor,time in adjList[node]:
                if curr_total + time < minTimes[neighbor]:
                    minTimes[neighbor] = curr_total + time
                    heappush(heap, (minTimes[neighbor], neighbor))
        maxTime = 0
        for minTime in minTimes[1:]:
            if minTime == float("inf"):
                return -1
            maxTime = max(maxTime, minTime)
        return int(maxTime)
