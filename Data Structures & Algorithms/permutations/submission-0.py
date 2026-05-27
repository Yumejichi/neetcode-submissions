class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = [False] * len(nums)
        curr_perm = [0] * len(nums)
        def dfs(index):
            if index == len(nums):
                res.append(curr_perm[:])
            
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    curr_perm[index] = num
                    dfs(index+1)
                    used[i] = False
        dfs(0)
        return res

            