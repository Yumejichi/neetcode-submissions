
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        res = []

        def backtrack(row, curr):
            if row == n:
                res.append(["".join (r) for r in curr])
                return 
            
            for col in range(n):
                if col in cols or row-col in diag1 or row+col in diag2:
                    continue
                curr[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                
                backtrack(row+1,curr)
                curr[row][col] = "."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        grid = [["."]* n for _ in range(n)]
        backtrack(0, grid)
        return res
            
        