class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numToIndex = {}
        # for i, num in enumerate(numbers):
        #     if target - num in numToIndex:
        #         return [numToIndex[target - num], i+1]
        #     numToIndex[num] = i+1

        # since sorted, we can use two pointers
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return[l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
                
        