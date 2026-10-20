from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapify(maxHeap)

        while len(maxHeap) > 1:
            num1 = -heappop(maxHeap)
            num2 = -heappop(maxHeap)
            if num1 == num2:
                continue
            heappush(maxHeap, -abs(num1-num2))

        return -maxHeap[0] if maxHeap else 0
