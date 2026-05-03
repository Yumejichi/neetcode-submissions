class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            s2_counts[index] += 1
            if s2_counts[index] == s1_counts[index]:
                matches += 1
            # if originally matched:
            if s1_counts[index] + 1 == s2_counts[index]:
                matches -= 1
            
            left = ord(s2[l]) - ord('a')
            s2_counts[left] -= 1
            if s1_counts[left] == s2_counts[left]:
                matches += 1
            if s1_counts[left] - 1 == s2_counts[left]:
                matches -= 1
            
            l += 1
        
        return matches == 26


