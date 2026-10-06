class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()

        l = 0
        seen.add(s[l])
        maxLen = 1
        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen

