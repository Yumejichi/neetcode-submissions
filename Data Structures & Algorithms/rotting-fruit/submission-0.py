class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row == ROWS or col == COLS or min(row, col) < 0:
                        continue
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            res += 1
        return res if fresh == 0 else -1