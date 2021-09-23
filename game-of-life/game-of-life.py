class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        def count_nei(r,c):
            nei = 0
            for i in range(r-1,r+2): #
                for j in range(c-1,c+2): # 
                    if (r==i and c==j) or i < 0 or j < 0 or i == len(board) or j == len(board[0]):
                        continue

                    elif board[i][j] in [1,3]:
                        nei+=1
            return nei


        for r in range(len(board)):
            for c in range(len(board[0])):
                nei = count_nei(r,c)
                if nei < 2:
                    if board[r][c] == 1:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0

                elif board[r][c] == 1 and nei in [2,3]:
                    board[r][c] = 3

                elif board[r][c] == 0 and nei == 3:
                    board[r][c] = 2

                else:
                    if board[r][c] == 1:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1