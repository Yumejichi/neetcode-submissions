class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:

        res = []

        index = 0
        while index < len(s):
            length = 0
            len_str = ""
            while s[index] != "#":
                len_str += s[index]
                index += 1
            length = int(len_str)
            # skip #
            index += 1
            # get the string
            string = s[index:index+length]
            res.append(string)
            index = index + length
        return res
