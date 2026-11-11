class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target, remainder = total//2, total %2
        if remainder!=0:
            return False
        
        n = len(nums)
        #dp[i][j]: if i elements can sum to j
        dp = [[False] * (target+1) for _ in range(n+1)] 
        dp[0][0] = True

        for i in range(1, n+1):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j] # we don't use the current one
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]

