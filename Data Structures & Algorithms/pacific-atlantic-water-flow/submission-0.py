class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        ROWS, COLS = len(heights), len(heights[0])

        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, ocean):
            if ocean[r][c]:
                return
            ocean[r][c] = True
            for dr, dc in dirs:
                row, col = r+dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS:
                    if heights[row][col] >= heights[r][c]:
                        dfs(row, col, ocean)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res