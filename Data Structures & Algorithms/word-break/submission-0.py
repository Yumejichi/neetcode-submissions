class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1) # can be break down till index i
        dp[n] = True

        for i in range(n-1, -1,-1):
            for word in wordDict:
                if len(word) + i <= n and s[i:len(word)+i] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break
        return dp[0]


            
            


