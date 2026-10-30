from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)] # time, r , c
        n = len(grid)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        while heap:
            time, r, c = heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == n-1 and c == n-1:
                return time

            for dr, dc in dirs:
                x,y=r+dr,c+dc
                if 0 <= x < n and 0 <= y < n and (x,y) not in visited:
                    maxTime = max(time, grid[x][y])
                    heappush(heap, (maxTime, x, y))

            

