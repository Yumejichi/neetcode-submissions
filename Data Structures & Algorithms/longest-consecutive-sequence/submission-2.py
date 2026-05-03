class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) <= 1):
            return len(nums)
        nums.sort()

        maxLen = 1

        l, r = 0, 0

    

        while r < len(nums):
            same = 0
            length = 1
            while  r < len(nums)-1 and nums[r] == nums[r + 1] - 1 or r < len(nums)-1 and nums[r] == nums[r + 1]:
                if nums[r] != nums[r + 1]:
                    length += 1
                r += 1

            if length > maxLen:
                maxLen = length
            if l == r:
                # no consecutive
                l += 1
                r += 1
            l = r
        
        return maxLen
            
