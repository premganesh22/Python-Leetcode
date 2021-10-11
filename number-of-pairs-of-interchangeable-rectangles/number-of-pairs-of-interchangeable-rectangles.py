class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dic = defaultdict(int)
        for i in range(len(rectangles)):
            val = rectangles[i][0]/rectangles[i][1]
            dic[val]+=1
        
        count = 0
        for k,v in dic.items():
            count+=(v*(v-1))//2
        return count
        