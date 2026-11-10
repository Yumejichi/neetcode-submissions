class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]: longest increasing subsequence ending at index i
        n = len(nums)
        dp = [1] * n
        maxLen = 1


        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    maxLen = max(maxLen, dp[i])
        return maxLen