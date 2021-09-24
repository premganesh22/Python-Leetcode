class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        final = []
        start,end = 0,1
        for i in firstList:
            for j in secondList:
                if i[end] >= j[start] and i[start]<=j[end]:
                    final.append([max(i[start],j[start]),min(i[end],j[end])])

        return final