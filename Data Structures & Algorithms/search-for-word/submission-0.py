class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c, curr):

            if r == ROWS or c == COLS or min(r, c) < 0 or (r, c) in visit:
                return
            curr += board[r][c]
            visit.add((r, c))
            if curr == word:
                return True
            found = (
                dfs(r + 1, c, curr) or
                dfs(r - 1, c, curr) or
                dfs(r, c + 1, curr) or
                dfs(r, c - 1, curr)
            )
            visit.remove((r, c))
            return found

        
        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, "")
                if res:
                    return True
        return False