import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isFinishedEating(speed, h):
            total = 0
            for bananas in piles:
                time = math.ceil(bananas / speed)
                total += time
            return total <= h
        
        low, high = 1, max(piles) # speed to eat
        res = high
        while low <= high:
            mid = (low + high) // 2
            if isFinishedEating(mid, h):
                # we can eat slower
                res = mid # record the las possible speed
                high = mid - 1
            else:
                # we could not finish eating, need to increase speed
                low = mid + 1
        return res



        