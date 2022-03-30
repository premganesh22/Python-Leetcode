class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table = [[1]*i for i in range(1,numRows+1)]
        for rows in range(2,numRows):
            for col in range(1,len(table[rows])-1):
                table[rows][col] = table[rows-1][col] + table[rows-1][col-1]
        return table