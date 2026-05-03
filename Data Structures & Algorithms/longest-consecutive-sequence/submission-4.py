class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # sorting
        sortedNums = sorted(nums)
        maxLen = 1
        curr = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i-1] + 1:
                curr += 1
            elif sortedNums[i] == sortedNums[i-1]:
                continue
            else:
                maxLen = max(maxLen, curr)
                curr = 1
        return max(maxLen, curr)
