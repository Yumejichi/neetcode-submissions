from heapq import heappush ,heappop
class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap store all small nums, we always keep small larger
        self.large = [] #minheap store all large nums
        

    def addNum(self, num: int) -> None:
        if len(self.large) == 0 or num < self.large[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num) 
        if len(self.small) < len(self.large):
            val = heappop(self.large)
            heappush(self.small, -val)
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)


    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] + -self.small[0]) /2
        else:
            return -self.small[0]