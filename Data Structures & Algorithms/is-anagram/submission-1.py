class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict()
        for c in s:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
        for c in t:
            if c not in chars:
                return False
            chars[c] -= 1
        
        for val in chars.values():
            if val != 0:
                return False
        return True