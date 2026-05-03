class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [] stack for current 

        res = [0] * len(temperatures)
        stack = [] # (temp, index)


        for i, tmp in enumerate(temperatures):
            # see if the stack is empety
            while stack and stack[-1][0] < tmp:
                t, index = stack.pop()
                res[index] = i - index
            stack.append((tmp, i))

        return res 