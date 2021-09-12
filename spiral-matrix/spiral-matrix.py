class Solution(object):
    def spiralOrder(self, lista):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top,left = 0,0
        bottom, right = len(lista)-1, len(lista[0])-1
        direction = 0
        output = []
        while len(output) < len(lista)*len(lista[0]):
            if direction == 0:
                for i in range(left,right+1):

                    output.append(lista[top][i])
                top+=1
            if direction == 1:
                for i in range(top,bottom+1):
                    output.append(lista[i][right])
                right-=1
            if direction == 2:
                for i in range(right,left-1,-1):
                    output.append(lista[bottom][i])
                bottom-=1
            if direction == 3:
                for i in range(bottom,top-1,-1):
                    output.append(lista[i][left])
                left+=1
            direction = (direction+1)%4
        return output