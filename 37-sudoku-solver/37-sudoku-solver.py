class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_next_element(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return row,col
            return None,None

        def is_valid(board,row,col):
            guess = board[row][col]

            #Row
            for r in range(9):
                if board[row][r] == guess and r != col:
                    return False
            #Col
            for c in range(9):
                if board[c][col] == guess and c != row:
                    return False

            #three matrix
            row_idx = (row//3) * 3
            col_idx = (col//3) * 3

            for r in range(row_idx,row_idx+3):
                for c in range(col_idx,col_idx+3):
                    if board[r][c] == guess and r != row and c!= col:
                        return False
            return True

        def sudaku(board,row,col):

            if not row == -1 and not is_valid(board,row,col):
                return 

            row,col = find_next_element(board)

            if row is None:
                return True

            for idx in range(1,10):
                board[row][col] = str(idx)
                if sudaku(board,row,col):
                    return True
                board[row][col] = '.'
            return False
        sudaku(board,-1,-1)