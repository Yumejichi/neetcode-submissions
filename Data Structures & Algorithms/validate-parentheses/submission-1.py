class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        closeToOpen = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        

        for item in s:
            if item in closeToOpen:
                if stack and stack[-1] == closeToOpen[item]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(item)
        
        return stack == []