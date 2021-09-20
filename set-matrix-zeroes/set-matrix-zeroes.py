class Solution(object):
    def setZeroes(self, lista):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        output = []
        for row in range(len(lista)):
            for column in range(len(lista[0])):
                if lista[row][column] == 0:
                    rows.append(row)
                    columns.append(column)

        for row in range(len(lista)):
            for column in range(len(lista[0])):
                if row in rows or column in columns:                    
                    lista[row][column] = 0
            
        return lista