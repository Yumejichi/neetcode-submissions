from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []

        for i in range(k):
            heappush(maxHeap, (-nums[i], i))

        l = 0
        res = []
        res.append(-maxHeap[0][0])

        for r in range(k, len(nums)):
            heappush(maxHeap, (-nums[r], r))
            l += 1
            while maxHeap[0][1] < l:
                heappop(maxHeap)
            res.append(-maxHeap[0][0])
        return res


