class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0

        total = 0

        l, r = 0, len(height)-1
        while l < r:
            currL, currR = height[l], height[r]
            maxL = max(maxL, currL)
            maxR = max(maxR, currR)

            if currL < currR:
                if currL < maxL and currL < maxR:
                    total += min(maxL, maxR) - currL
                l += 1
            else:
                if currR < maxL and currR < maxR:
                    total += min(maxL, maxR) - currR
                r -= 1
            
            
            
        return total