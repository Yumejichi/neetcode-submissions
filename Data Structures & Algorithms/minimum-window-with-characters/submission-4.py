class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counts_s = {}
        counts_t = {}

        need = 0

        for i in range(len(t)):
            if t[i] not in counts_t:
                need += 1
            counts_t[t[i]] = counts_t.get(t[i], 0) + 1
        
        l = 0
        res = ""
        best_start = 0
        min_len = float("inf")
        for r in range(len(s)):
            counts_s[s[r]] = counts_s.get(s[r], 0) + 1
            if  s[r] in counts_t and counts_s[s[r]] == counts_t[s[r]]:
                need -= 1
            while need == 0:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    best_start = l
                counts_s[s[l]] -= 1
                # previously meet the need
                if s[l] in counts_t and counts_s[s[l]] + 1 == counts_t[s[l]]:
                    need += 1
                l += 1
        return s[best_start:best_start+min_len] if min_len != float("inf") else ""

            
            
        
        