class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path.copy())
                return

            # we add curr node
            backtrack(index+1, path+[nums[index]])

            # we do not add curr node
            backtrack(index+1, path)
        backtrack(0,[])

        return res
            