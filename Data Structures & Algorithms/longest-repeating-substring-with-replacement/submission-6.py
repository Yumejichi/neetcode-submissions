class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use sliding window and track how many replacement we have done
        # we move l until the s[l] counts is the largest and not equal to the prev max letter
        if not s:
            return 0
        counts = {}
        l = 0
        maxLen = 0
        maxFrequency = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxFrequency = max(maxFrequency, counts[s[r]])
            while maxFrequency + k < r-l+1:
                counts[s[l]] -= 1
                l += 1
                # maxFrequency = max(counts.values())
            maxLen = max(maxLen, r-l+1)
        return maxLen
                
                
