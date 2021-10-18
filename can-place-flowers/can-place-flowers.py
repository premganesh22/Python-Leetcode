class Solution:
    def canPlaceFlowers(self, lista: List[int], n: int) -> bool:
        index = 1
        lista.insert(0,0)
        lista.append(0)
        count = 0
        if n == count:
            return True
            
        
        while index < len(lista)-1:
            if lista[index] != 1 and lista[index-1] == 0 and lista[index+1] == 0:

                lista[index] = 1
                count+=1
            if n == count:
                return True
               
            index+=1
        return False