class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #from heap import heapify
        for i in points:
            sqrt = i[0]**2 + i[1]**2
            i.insert(0,sqrt)
        import heapq
        heapq.heapify(points)
        output = []
        for num in range(k):
            temp = heapq.heappop(points)
            output.append([temp[1],temp[2]])
        return output
        