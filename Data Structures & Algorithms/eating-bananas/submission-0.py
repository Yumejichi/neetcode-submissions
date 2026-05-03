class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the speed can be from 1 to max(piles)

        r = max(piles)

        # need to find the smallest speed but can finish eating everything
        # use binary search to try the speed from 1 to high

        l = 1
        res = r

        while l <= r:
            # check if can finish eating
            total = 0
            # set the speed as mid
            k = (l + r) // 2
            for pile in piles:
                total += math.ceil(float(pile) / k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
            



        