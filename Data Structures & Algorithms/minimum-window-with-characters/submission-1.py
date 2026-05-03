class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = Counter(t)
        need = len(count_t)
        have = 0

        l = 0
        count_s = {}
        min_len = float("inf")
        res = ""
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < min_len:
                    res = s[l:r+1]
                    min_len = r-l + 1
                
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            
        
        return res
            

