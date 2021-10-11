class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dic_row = defaultdict(list)
        dic_column = defaultdict(list)
        dic_box = defaultdict(list)
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                val = board[row][column]
            
                if val == '.':
                    continue
                if (val in dic_row[row] or val in dic_column[column] or val in dic_box[(row//3,column//3)]):
                    print(val)
                    return False
                dic_row[row].append(val)
                dic_column[column].append(val)
                dic_box[(row//3,column//3)].append(val)
        return True
        