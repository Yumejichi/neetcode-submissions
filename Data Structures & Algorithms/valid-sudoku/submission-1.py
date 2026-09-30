class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use a set to trak each row, col and square
        # for square, we have 9 suqares each can be located by useing (row//3, col//3)
        seen_rows = [set() for _ in range(9)]
        seen_cols = [set() for _ in range(9)]
        seen_squares = {
            (r,c): set()
            for r in range(3)
            for c in range(3)
        }
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen_rows[row] or board[row][col] in seen_cols[col] or board[row][col] in seen_squares[(row//3, col//3)]:
                    return False
                # check square:
                seen_rows[row].add(board[row][col])
                seen_cols[col].add(board[row][col])
                seen_squares[(row//3, col//3)].add(board[row][col])
        return True



