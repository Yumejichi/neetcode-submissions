class Solution:
    def __init__(self):
        self.separations = []
        self.encoded = ""

    def encode(self, strs: List[str]) -> str:
        for string in strs:
            self.separations.append(len(string))
            self.encoded += string
        print(self.encoded)
        return self.encoded

    def decode(self, s: str) -> List[str]:
        res = []
        prev = 0
        for sep in self.separations:
            string = self.encoded[prev:prev+sep]
            res.append(string)
            prev = len(string) + prev
        return res

