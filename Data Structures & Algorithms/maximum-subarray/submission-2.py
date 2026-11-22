class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            # extend or restart
            total = max(total + nums[i], nums[i])
            res = max(res, total)
        return res