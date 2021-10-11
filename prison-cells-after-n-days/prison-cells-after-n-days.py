class Solution:
    def swap_nums(self,cells):
    
        new_cells = [0]*len(cells)
        for i in range(1,7):
            if cells[i-1] == cells[i+1]:
                new_cells[i] = 1
        return new_cells
    
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        dic = {}
        for i in range(n):
            if not str(cells) in dic:
                dic[str(cells)] = i
                cells = self.swap_nums(cells)
            else:
                print(i)
                length = i - dic[str(cells)] 
                return self.prisonAfterNDays(cells,(n-i)%length)
        return cells
        