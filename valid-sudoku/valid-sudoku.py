class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        row_col = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in row_col[(r//3,c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    row_col[(r/3,c/3)].add(board[r][c])
        return True      