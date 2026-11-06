class Solution:
    def numDecodings(self, s: str) -> int:
        # try to do with backtrack first

        memo = {}

        def dfs(index):
            if index == len(s):
                return 1

            if s[index] == "0":
                return 0

            if index in memo:
                return memo[index]

            # use one digit
            ways = dfs(index+1)

            # use two digits:
            if index+1 < len(s) and int(s[index:index+2]) <= 26:
                ways += dfs(index+2)
            memo[index] = ways
            return memo[index]
        return dfs(0)

