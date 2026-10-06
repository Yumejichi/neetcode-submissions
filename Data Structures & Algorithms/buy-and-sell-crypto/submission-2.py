class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use sliding window
        # l -> keep track the min seen so far
        # r -> we move this and we update max

        l = 0
        maxProfit = 0
        for r in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxProfit
            
            