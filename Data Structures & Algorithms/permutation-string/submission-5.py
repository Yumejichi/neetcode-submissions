class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use the match to count how many letters matches, it matches == 26 it means we have the correct permutation
        if len(s2) < len(s1):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            s2_index = ord(s2[i]) - ord("a")
            s1_counts[s1_index] += 1
            s2_counts[s2_index] += 1

        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            right = ord(s2[r]) - ord("a")

            s2_counts[right] += 1
            if s2_counts[right] == s1_counts[right]:
                matches += 1
            elif s2_counts[right] - 1 == s1_counts[right]:
                matches -= 1
            
            left = ord(s2[l]) - ord("a")
            s2_counts[left] -= 1
            if s2_counts[left] == s1_counts[left]:
                matches += 1
            elif s2_counts[left] + 1 == s1_counts[left]:
                matches -= 1
            l += 1
        return matches == 26

