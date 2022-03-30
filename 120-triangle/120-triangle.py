class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        table = [[0]*i for i in range(1,len(triangle)+1)]
        table[0][0] = triangle[0][0]
        for row in range(1,len(triangle)):
            table[row][0] = table[row-1][0]+triangle[row][0]
            table[row][-1] = table[row-1][-1]+triangle[row][-1]

        for row in range(2,len(triangle)):
            for col in range(1,len(table[row])-1):
                table[row][col] = min(table[row-1][col],table[row-1][col-1])+triangle[row][col]
        return min(table[-1])