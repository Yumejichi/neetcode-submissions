class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(arr):
            l, r = 0, len(arr)-1

            while l < r:
                if arr[l] == arr[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start, len(s)):
                piece = s[start:end+1]
                if isPalindrome(piece):
                    path.append(piece)
                    dfs(end+1, path)
                    path.pop()



        dfs(0,[])
        return res
