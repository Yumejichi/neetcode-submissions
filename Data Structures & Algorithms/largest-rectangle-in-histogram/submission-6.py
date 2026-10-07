class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[height, startIndex]
        maxArea = 0

        for i, h in enumerate(heights):
            if stack and stack[-1][0] < h or not stack:
                # heigher, we append to stack
                stack.append([h, i])
            # we try all possible posibilityies in the stack:

            else:
                # when the element reduces, we update the prev height
                # keep poping until the prev height is lower:
                prevIndex = i
                while stack and stack[-1][0] > h:
                    height, prevIndex = stack.pop()
                    # update max area if eligible:
                    maxArea = max(maxArea, height*(i - prevIndex))
                stack.append([h, prevIndex])
                
        for height, index in stack:
            area = (i-index+1) * height
            maxArea = max(maxArea, area)
        return maxArea
                
