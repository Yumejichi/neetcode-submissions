class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = defaultdict()
        
        for i in range(len(nums)):
            num = nums[i]
            if target - num in numToIndex:
                return [numToIndex[target - num], i]
            else:
                numToIndex[num] = i