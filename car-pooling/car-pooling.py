class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l=[]
        for ppl,start,end in trips:
            l.append([start,ppl])
            l.append([end,-ppl])

        l.sort()
        candidate=0
        for _,ppl in l:
            candidate+=ppl
            if candidate > capacity:
                return False
        return True
        