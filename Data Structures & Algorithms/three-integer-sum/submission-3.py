class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                if num + nums[l] + nums[r] == 0:
                    if (num, nums[l], nums[r]) not in res:
                        res.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return list(res)
