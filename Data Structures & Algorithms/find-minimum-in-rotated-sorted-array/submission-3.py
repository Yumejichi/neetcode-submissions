class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find first true
        index = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # we find the first num that is num < nums[-1]
            if nums[mid] < nums[-1]:
                index = mid
                r = mid - 1
            else:
                l = mid + 1
        return nums[index]
  

        