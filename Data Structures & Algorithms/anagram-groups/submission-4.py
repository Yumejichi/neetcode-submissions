class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for letter in s:
                index = ord(letter)-ord("a")
                letters[index] += 1
            anagrams[tuple(letters)].append(s)
        return list(anagrams.values())
