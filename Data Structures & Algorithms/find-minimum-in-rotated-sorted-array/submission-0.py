class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        # find the boudry for first true where 
        # first <= nums[-1]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[-1]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return nums[res]


