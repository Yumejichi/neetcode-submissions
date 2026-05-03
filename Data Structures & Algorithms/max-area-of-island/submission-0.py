class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return count

        max_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_count = dfs(r, c)
                    max_count = max(max_count, curr_count)

        return max_count
