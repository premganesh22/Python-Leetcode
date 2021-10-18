class Solution:
    def eraseOverlapIntervals(self, lista: List[List[int]]) -> int:
        lista = sorted(lista,key=lambda x:x[1])
        
        count = 0
        last_end = lista[0][1]
        for start,end in lista[1:]:

            if last_end <= start:
                last_end = end
            else:
                count+=1
        return count