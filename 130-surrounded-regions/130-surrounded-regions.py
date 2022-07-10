class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [[0,1], [0,-1], [1, 0], [-1, 0]]
        def get_nei(x,y):
            output = []
            for m, n in direction:
                if 0 <= x+m < len(board) and 0 <= y+n < len(board[0]):
                    output.append([x+m, y+n])
            return output
        
        def dfs(x,y):
            board[x][y] = 'T'
            for m,n in get_nei(x,y):
                if board[m][n] == 'O':
                    dfs(m,n)
                
        
        
        for x in [0, len(board)-1]:
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    dfs(x, y)
                
        for x in range(1,len(board)):
            for y in [0, len(board[0])-1]:
                print(x,y)
                if board[x][y] == 'O':
                    dfs(x, y)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'T':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'
                    
        
                    
        
        
        