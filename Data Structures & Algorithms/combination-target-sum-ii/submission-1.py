class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, total, path):
            if target == total:
                res.append(path.copy())
                return
            if index == len(candidates) or total > target:
                return
            
            # for i in range(index, len(candidates)):
            #     if i > index and candidates[i] == candidates[i-1]:
            #         continue
            #     path.append(candidates[i])
            #     backtrack(i+1, total+candidates[i],path)
            #     path.pop()
            # include curr:
            backtrack(index+1, total+candidates[index], path+[candidates[index]])
            # exclude current one:
            next_index = index+1
            while next_index < len(candidates) and candidates[next_index] == candidates[next_index-1]:
                next_index+=1
            backtrack(next_index, total, path)
        backtrack(0,0,[])
        return res