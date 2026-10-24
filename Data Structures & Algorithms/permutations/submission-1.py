class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(index, path):
            if not 0<=index<len(nums):
                return
            if len(seen) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i not in seen and i != index:
                    seen.add(i)
                    path.append(nums[i])
                    backtrack(i,path)
                    path.pop()
                    seen.remove(i)
        for i in range(len(nums)):
            seen.add(i)
            backtrack(i,[nums[i]])
            seen.remove(i)
        return res