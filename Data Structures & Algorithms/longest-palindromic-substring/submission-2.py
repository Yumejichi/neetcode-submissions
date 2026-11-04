class Solution:
    def longestPalindrome(self, s: str) -> str:
        # store if s[l:r+1] is a plindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""
        # for each dp[i][j] we need dp[i+1][j-1]
        for l in range(n-1,-1,-1):
            for r in range(l,n):
                if s[l] != s[r]:
                    continue
                if r - l <= 1:
                    dp[l][r] = True
                else:
                    dp[l][r] = dp[l+1][r-1]
                if dp[l][r] and r-l+1 > len(res):
                    res = s[l:r+1]
        return res