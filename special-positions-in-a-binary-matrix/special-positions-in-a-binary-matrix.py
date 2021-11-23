class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    rows[row]+=1
                    cols[col]+=1
        output=0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:  
                    if rows[row] <= 1 and cols[col] <=1:
                        output+=1
        return output
                    