class Solution:
    def longestPalindrome(self, s: str) -> str:

        # we think each letter as the central and check if there is a palindrome from it:
        maxRes = ""
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:

                while l >= 0 and r < len(s) and l <= r and s[l]==s[r]:

                    if r-l+1 > len(maxRes):
                        maxRes = s[l:r+1]
                    l -= 1
                    r += 1
            
        return maxRes


