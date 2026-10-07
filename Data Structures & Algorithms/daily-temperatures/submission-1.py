class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        currMin = []
        stack = [] # (temp, index)

        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if currMin and temp > currMin[-1]:
                remains = []
                while stack and temp > currMin[-1]:
                    pastTemp, index = stack.pop()
                    if pastTemp >= temp:
                        remains.append((pastTemp, index))
                    else:
                        res[index] = i-index
                    currMin.pop()

                # we put the remians back:
                while remains:
                    pastTemp, index = remains.pop()
                    stack.append((pastTemp, index))
                    if not currMin:
                        currMin.append(pastTemp)
                    else:
                        currMin.append(min(pastTemp, currMin[-1]))
            stack.append((temp, i))
            if currMin:
                currMin.append(min(currMin[-1], temp))
            else:
                currMin.append(temp)
        return res
