class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, total, path):
            if total == target:
                res.append(path[:])
            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, total + candidates[i], path)
                path.pop()

        candidates.sort()
        dfs(0, 0, [])
        return res