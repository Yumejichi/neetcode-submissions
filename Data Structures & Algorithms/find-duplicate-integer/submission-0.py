class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        first_true_index = -1
        while l <= r:
            mid = (l + r) // 2
            counts = sum(1 for num in nums if num <= mid)

            if counts <= mid:
                # duplicate exists
                l = mid + 1
            else:
                first_true_index = mid
                r = mid - 1
        return first_true_index