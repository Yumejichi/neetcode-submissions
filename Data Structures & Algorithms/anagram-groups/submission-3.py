class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            counts = [0] * 26

            for c in string:
                num = ord(c) - ord("a")
                counts[num] += 1
            anagrams[tuple(counts)].append(string)
        return [val for val in anagrams.values()]