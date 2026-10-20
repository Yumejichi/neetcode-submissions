from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        maxHeap = [-count for count in counts.values()]
        heapify(maxHeap)


        cooldown = deque()
        curr_time = 0
        while maxHeap or cooldown:
            curr_time += 1
            while cooldown and cooldown[0][0] <= curr_time:
                ready_time, remaining = cooldown.popleft()
                heappush(maxHeap, -remaining)
            if maxHeap:
                remaining = -heappop(maxHeap) - 1
                if remaining > 0:
                    cooldown.append((curr_time+n+1, remaining))
        return curr_time


