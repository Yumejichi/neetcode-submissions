class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # sorting
        # sortedNums = sorted(nums)
        # maxLen = 1
        # curr = 1

        # for i in range(1, len(sortedNums)):
        #     if sortedNums[i] == sortedNums[i-1] + 1:
        #         curr += 1
        #     elif sortedNums[i] == sortedNums[i-1]:
        #         continue
        #     else:
        #         maxLen = max(maxLen, curr)
        #         curr = 1
        # return max(maxLen, curr)

        # use O(n) method:
        maxLen = 0
        numSet = set(nums)

        # check if the number starts from the current one and if so, check how many:
        for num in nums:
            if num - 1 not in numSet:
                curr = num
                currLen = 1
                while curr + 1 in numSet:
                    curr += 1
                    currLen += 1
                maxLen = max(maxLen, currLen)
        
        return maxLen


