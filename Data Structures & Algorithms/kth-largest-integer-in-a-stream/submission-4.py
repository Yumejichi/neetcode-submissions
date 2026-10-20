from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for i in range(min(k, len(nums))):
            heappush(self.minHeap, nums[i])
        for num in nums[k:]:
            if num > self.minHeap[0]:
                heappop(self.minHeap)
                heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        if self.minHeap and len(self.minHeap) >= self.k:
            if val > self.minHeap[0]:
                heappop(self.minHeap)
                heappush(self.minHeap, val)
        else:
            heappush(self.minHeap, val)
        return self.minHeap[0]
        
