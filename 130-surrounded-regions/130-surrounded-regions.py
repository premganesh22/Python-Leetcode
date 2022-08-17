class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def get_adjacent(row,col):
            output = []
            for x, y in [[1,0], [-1,0], [0,1], [0,-1]]:
                if 0 <= row+x < len(board) and 0 <= col+y < len(board[0]) and board[row+x][col+y] == 'O':
                    output.append([row+x, col+y])
            return output
        
        def dfs(row,col):
            visited.add((row,col))
            board[row][col] = '-1'
            for x, y in get_adjacent(row,col):
                if not (x,y) in visited:
                    dfs(x,y)
                    
        visited = set()
        
        for row in [0, len(board)-1]:
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (row,col) not in visited:
                            
                    dfs(row,col)
        
        for row in range(len(board)):
            for col in [0, len(board[0])-1]:
                    if board[row][col] == 'O' and (row,col) not in visited:
                            
                        dfs(row,col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '-1':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'        