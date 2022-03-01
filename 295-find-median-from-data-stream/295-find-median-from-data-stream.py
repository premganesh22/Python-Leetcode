class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        #check where the element has to go
        if not self.max_heap or -self.max_heap[0]>=num:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
        
        #Balance the heap
        if len(self.max_heap) > len(self.min_heap)+1:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-temp)
            
        elif len(self.max_heap)+1 < len(self.min_heap):
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-temp)

    def findMedian(self) -> float:
        if len(self.min_heap)  == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()