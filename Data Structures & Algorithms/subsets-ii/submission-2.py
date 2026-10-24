class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path.copy())
                return
            
            # for i in range(index, len(nums)):
            #     if i > index and nums[i] == nums[i-1]:
            #         continue
            #     path.append(nums[i])
            #     backtrack(i+1, path)
            #     path.pop()
            # add curr:
            backtrack(index+1, path + [nums[index]])
            # exclude curr
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[next_index-1]:
                next_index+=1
            backtrack(next_index, path)

        backtrack(0, [])

        return res
