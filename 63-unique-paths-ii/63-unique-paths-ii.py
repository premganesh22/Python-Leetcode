class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        table = [[0]*(len(obstacleGrid[i])) for i in range(len(obstacleGrid))]
        
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        #row
        for row in range(len(table)):
            if obstacleGrid[row][0] != 1:
                table[row][0] = 1
            else:
                break
        
        for col in range(len(table[0])):
            if obstacleGrid[0][col] != 1:
                table[0][col] = 1
            else:
                break
        
        print(table)
        
        for i in range(1,len(table)):
            for j in range(1,len(table[0])):
                if obstacleGrid[i][j] == 1:
                    table[i][j] = 0
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
                
        return table[-1][-1]
        