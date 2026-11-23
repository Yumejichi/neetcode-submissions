class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            farthest = min(i + nums[i], n - 1)
            
            for j in range(i + 1, farthest + 1):
                if dp[j]:
                    dp[i] = True
                    break
                    
        return dp[0]

