class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] <= nums[1]:
                return nums[0]
            return nums[1]

        l, r = 0, len(nums) - 1
        # we need to find the first True val where 
        # num on the left is bigger than it
        # num on the right is bigger than it
        res = nums[l]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
                res = nums[mid]
            else:
                l = mid+1
        return nums[r]


  

        