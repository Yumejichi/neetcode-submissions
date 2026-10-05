class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        maxLen = 0


        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                end = num
                while end in numSet:
                    end += 1
                maxLen = max(maxLen, end - num)
        return maxLen

        