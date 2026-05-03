class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(l, r, nums, target):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid + 1, r, nums, target)
            else:
                return binarySearch(l, mid - 1, nums, target)
        
        return binarySearch(0, len(nums) - 1, nums, target)