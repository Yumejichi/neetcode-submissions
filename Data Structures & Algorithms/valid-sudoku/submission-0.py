class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check the row
        for row in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[row][j] in seen:
                    return False 
                if board[row][j] != ".":
                    seen.add(board[row][j])

        # check the column
        for col in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][col] in seen:
                    return False
                if board[i][col] != ".":
                    seen.add(board[i][col])
        
        # check the square:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


        