class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars1 = {}
        chars2 = {}

        for c in s:
            chars1[c] = chars1.get(c, 0) + 1
        
        for c in t:
            chars2[c] = chars2.get(c, 0) + 1

        return chars1 == chars2