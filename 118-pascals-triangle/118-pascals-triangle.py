class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        table = [[1]*i for i in range(1,numRows+1)]
        
        for i in range(2,len(table)):
            for j in range(1,len(table[i])-1):
                table[i][j] = table[i-1][j-1] + table[i-1][j]
        
        return table
        