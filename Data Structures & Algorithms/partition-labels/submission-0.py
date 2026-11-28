class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)

        currSet = set()
        curr = []
        res = []
        for letter in s:
            currSet.add(letter)
            curr.append(letter)
            counts[letter] -= 1
            if counts[letter] == 0:
                currSet.remove(letter)
                if len(currSet) == 0:
                    res.append(len(curr))
                    curr = []

        return res