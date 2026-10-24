class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        
        def dfs(index, path, r, c):
            if index == len(word)-1 and "".join(path)==word:
                return True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dr,dc in directions:
                x, y = r+dr, c + dc
                if 0<= x < rows and 0 <= y < cols and (x,y) not in seen:
                    seen.add((x,y))
                    path.append(board[x][y])
                    res = dfs(index+1, path, x, y)
                    if res:
                        return True
                    path.pop()
                    seen.remove((x,y))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    seen.add((r,c))
                    res = dfs(0,[word[0]],r,c)
                    seen.remove((r,c))
                    if res:
                        return True
        return False

