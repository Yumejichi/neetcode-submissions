class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle empty input case
        if not digits:
            return []
      
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in digit_to_letters[digits[i]]:
                backtrack(i+1, curr+c)
        res = []
        backtrack(0, "")
        return res
      