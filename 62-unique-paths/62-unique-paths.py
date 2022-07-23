class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1]*n for i in range(m)]
        
        for i in range(1,len(table)):
            for j in range(1,len(table[0])):
                table[i][j] = table[i-1][j] + table[i][j-1]
                
        return table[-1][-1]
        