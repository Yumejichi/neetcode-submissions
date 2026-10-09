class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # check if left is sorted or right is sorted:

            # left sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    #target > nums[mid] or target < nums[l]
                    l = mid + 1
            # right must be sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    #target > nums[r] or target < nums[mid]
                    r = mid - 1
        return -1

                    

                    
