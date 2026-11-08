class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        min_so_far = max_so_far = res = nums[0]

        for i in range(1,n):
            new_min = min(min_so_far*nums[i], max_so_far*nums[i], nums[i])
            new_max = max(max_so_far*nums[i], min_so_far*nums[i], nums[i])
            dp[i] = new_max
            max_so_far = new_max
            min_so_far = new_min
            res = max(res, max_so_far)
        return res