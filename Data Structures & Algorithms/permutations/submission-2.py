class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        used = [False] * len(nums)
        curr_perm = [0] * len(nums)

        def backtrack(index): # we fill each index
            if index == len(nums):
                res.append(curr_perm.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    # we need to use this to fill next one:
                    curr_perm[index] = nums[i]
                    used[i] = True
                    backtrack(index+1)
                    used[i] = False
        backtrack(0)
        return res
