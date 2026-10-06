class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(numbers):
            if target - num in numToIndex:
                return [numToIndex[target - num], i+1]
            numToIndex[num] = i+1
        