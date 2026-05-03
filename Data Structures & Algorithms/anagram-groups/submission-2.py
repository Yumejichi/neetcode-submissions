class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        combs = {}

        for word in strs:
            sortedWord = sorted(word)
            letters = [0] * 26
            for c in sortedWord:
                number = ord(c) - ord('a')
                # print(number)
                letters[number] += 1
            if tuple(letters) in combs:
                combs[tuple(letters)].append(word)
            else:
                combs[tuple(letters)] = []
                combs[tuple(letters)].append(word)
        # print(combs.values())
        return list(combs.values())


            
                