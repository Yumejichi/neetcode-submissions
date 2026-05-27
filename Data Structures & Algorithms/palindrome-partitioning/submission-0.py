class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            l, r = 0, len(string)-1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        curr = []
        def dfs(index):
            if index == len(s):
                res.append(curr[:])
                return

            for i in range(index, len(s)):
                if isPalindrome(s[index:i+1]):
                    curr.append(s[index:i+1])
                    dfs(i+1)
                    curr.pop()

        dfs(0)
        return res
                
            
            