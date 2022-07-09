class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def get_neighbours(m,n):
            output = []
            for x,y in directions:
                if 0<=m+x and m+x < len(matrix) and 0<=n+y and n+y < len(matrix[0]) and matrix[m][n] < matrix[m+x][n+y]:
                    output.append([m+x, n+y])
            return output
        
        
        max_length = [0]
        def dfs(m,n, cur_length):
            if visited[m][n] != 0:
                return visited[m][n]
            for x,y in get_neighbours(m,n):
                res = 1+ dfs(x,y, cur_length)
                visited[m][n] = max(res, visited[m][n])
            visited[m][n] = max(visited[m][n], cur_length+1)
            return visited[m][n]  
        
        visited = []
        for i in range(len(matrix)):
            visited.append([0]*len(matrix[i]))
        
        max_length = 0
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                length = dfs(m,n,0)
                max_length = max(max_length, length)
        
        return max_length
    
        