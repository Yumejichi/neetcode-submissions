class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # check if left is sorted or right is sorted
            if nums[l] <= nums[mid]: # left sorted
                if nums[l] <= target < nums[mid]:
                    # search left side
                    r = mid - 1
                else: # target < nums[l] or target > nums[mid]
                    l = mid + 1
            else: # right is sorter
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: # target < nums[mid] or target > nums[r]
                    r = mid - 1
        return -1

                
