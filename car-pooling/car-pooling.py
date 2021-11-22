class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        for cap, start, end in trips:
            l.append([start,cap])
            l.append([end,-cap])
            
        l.sort()
        candidate = 0
        for time,cap in l:
            candidate+=cap
            if candidate > capacity:
                return False
        return True