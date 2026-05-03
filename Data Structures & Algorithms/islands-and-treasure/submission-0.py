class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # traverse from a treasure chest(0)
        # use bfs to reack every cell we can from this chest

        ROWS, COLS = len(grid), len(grid[0])
        
        # put all of the 0 positions to the queue
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r, c))
        count = 0
        INF = 2147483647

        def get_neighbors(r, c):
            neighbors = []
            directions = [[0, 1], [0, -1], [1,0], [-1, 0]]
            for dr, dc in directions:
                new_r, new_c = dr + r, dc+c
                if min(new_r, new_c) < 0 or new_r==ROWS or new_c== COLS or grid[new_r][new_c] != INF or (new_r, new_c) in visited:
                    continue
                neighbors.append((new_r, new_c))
                visited.add((new_r, new_c))
            return neighbors

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = count
                for neighbor in get_neighbors(row, col):
                    r, c = neighbor
                    q.append(neighbor)
            count += 1