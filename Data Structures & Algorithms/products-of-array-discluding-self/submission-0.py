class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [[1] for i in range(len(nums))]
        pre = 1
        post = 1

        # store prefix
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        print(res)

        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res