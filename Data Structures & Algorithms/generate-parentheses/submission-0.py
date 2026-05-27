class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(index, open, close, curr):
            if index == n * 2:
                res.append("".join(curr))


            if open < n:
                curr.append("(")
                dfs(index+1, open+1, close, curr)
                curr.pop()
            
            if close < open:
                curr.append(")")
                dfs(index+1, open, close+1, curr)
                curr.pop()
        dfs(0, 0, 0, [])
        return res

            