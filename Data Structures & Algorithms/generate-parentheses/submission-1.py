class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        opens = 0
        closes = 0

        def helper(index, path):
            nonlocal opens, closes
            if index == 2 * n:
                res.append(path)
                return

            # add a open:
            if opens < n:
                opens += 1
                helper(index+1, path + "(")
                opens -= 1
            if closes < opens:
                closes += 1
                helper(index+1, path+")")
                closes -= 1

        helper(0,"")
        return res

            