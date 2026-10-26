class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def dfs(r,c):
            if (r,c) in visited or r<0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    dfs(r,c)
        return count
                