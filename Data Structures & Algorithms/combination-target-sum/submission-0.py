class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(total, path, i):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            for i in range(i, len(nums)):
                path.append(nums[i])
                dfs(total+nums[i], path, i)
                path.pop()

        dfs(0, [], 0)
        return res