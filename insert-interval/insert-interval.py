class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        output = []
        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]
        start = 0
        end = 1
        
        while i < len(intervals) and intervals[i][end] < new_interval_start:
            output.append(intervals[i])
            i+=1
            
        while i < len(intervals) and intervals[i][start] <= new_interval_end:
            new_interval_start = min(new_interval_start,intervals[i][start])
            new_interval_end = max(new_interval_end,intervals[i][end])
            i+=1
        output.append([new_interval_start,new_interval_end])
        
        while i < len(intervals):
            output.append(intervals[i])
            i+=1
        return output