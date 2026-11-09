class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # if we can break the word so far
        dp = [False] * (n+1)
        dp[n] = True # if we reach the end, then it is True

        for i in range(n-1,-1,-1):
            for word in wordDict:
                if len(word) + i <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break
        return dp[0]