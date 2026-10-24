class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(index, total, path):
            if index == len(nums) or total > target:
                return
            if total == target:
                res.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, total+nums[i],path)
                path.pop()
        backtrack(0,0,[])
        return res

