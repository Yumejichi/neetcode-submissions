class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        Pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        Atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # add to res if bot are true
        # we can either use dfs or bfs to do this but maybe bfs is better since we can explore all neighbors to gether
        # visited_pacific = set()
        # visited_atlantic = set()
        def bfs(r,c, ocean):
            q = deque([(r,c)])
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            while q:
                row,col = q.popleft()
                for dr, dc in dirs:
                    x,y = row+dr, col+dc
                    if 0<=x<ROWS and 0 <=y<COLS and ocean[x][y] == False and heights[x][y] >= heights[row][col]:
                        ocean[x][y] = True
                        q.append((x,y))

        # loop through pacific and atlantic
        for r in range(ROWS):
            Pacific[r][0] = True
            bfs(r,0,Pacific)

            # atlantic:
            Atlantic[r][COLS-1] = True
            bfs(r,COLS-1, Atlantic)
        for c in range(COLS):
            Pacific[0][c] = True
            bfs(0,c,Pacific)
            Atlantic[ROWS-1][c] = True
            bfs(ROWS-1, c, Atlantic)

        print(Pacific, Atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if Pacific[r][c] and Atlantic[r][c]:
                    res.append([r,c])
        return res
        

        



