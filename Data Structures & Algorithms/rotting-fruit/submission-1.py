from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        count = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and fresh > 0:
            curr_len = len(q)
            count += 1
            for _ in range(curr_len):
                r,c = q.popleft()
                for dr,dc in dirs:
                    x,y = r+dr, c+dc
                    if 0 <= x < ROWS and 0<=y<COLS and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x,y))
                        if fresh == 0:
                            break
        return count if fresh == 0 else -1




