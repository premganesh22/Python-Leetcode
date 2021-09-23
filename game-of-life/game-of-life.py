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

                    elif board[i][j] == 1:
                        nei+=1
            return nei

        output = []
        for r in range(len(board)):
            temp = []
            for c in range(len(board[0])):
                nei = count_nei(r,c)
                if nei < 2:
                    temp.append(0)
                elif board[r][c] == 1 and nei in [2,3]:
                    temp.append(1)
                elif board[r][c] == 0 and nei == 3:
                    temp.append(1)
                else:
                    temp.append(0)
            output.append(temp)
        
        for i in range(len(output)):
            for j in range(len(output[0])):
                board[i][j] = output[i][j]
        #return board