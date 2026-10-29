class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since we traverse the nearest, we do bfs

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r,c):
            q = deque([(r,c)])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            count = 0
            while q:
                curr_len = len(q)
                count += 1

                for _ in range(curr_len):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        x, y = row + dr, col + dc

                        if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] != -1 and grid[x][y] > count:
                            grid[x][y] = count
                            q.append((x,y))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r,c)


