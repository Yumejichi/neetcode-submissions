class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [] # keep the kth largest numbers
        self.k = k
        self.size = 0
        for num in nums:
            if self.size == self.k:
                if num > self.minHeap[0]:
                    heapq.heappush(self.minHeap, num)
                    heapq.heappop(self.minHeap)
            else:
                heapq.heappush(self.minHeap, num)
                self.size += 1

    def add(self, val: int) -> int:
        if self.size == self.k:
            if val > self.minHeap[0]:
                heapq.heappush(self.minHeap, val)
                heapq.heappop(self.minHeap)
        else:
            heapq.heappush(self.minHeap, val)
            self.size += 1
        return self.minHeap[0]