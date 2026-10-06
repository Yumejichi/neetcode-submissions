class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_letters = [0] * 26
        for c in s1:
            index = ord(c) - ord("a")
            s1_letters[index] += 1

        l = 0
        s2_letters = [0] * 26
        for r in range(len(s2)):
            right = ord(s2[r]) - ord("a")
            s2_letters[right] += 1
            while r-l+1 > len(s1):
                left = ord(s2[l]) - ord("a")
                s2_letters[left] -= 1
                l += 1
            if r-l+1 == len(s1) and s1_letters == s2_letters:
                return True
        return False



        