class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()

        res = []

        def backtrack(index, total, path):
            if index == len(nums) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return
            # for i in range(index, len(nums)):
            #     path.append(nums[i])
            #     backtrack(i, total+nums[i],path)
            #     path.pop()

            # include curr:
            backtrack(index, total+nums[index], path+[nums[index]])
            #not include curr:
            backtrack(index+1, total,path)
        backtrack(0,0,[])
        return res

