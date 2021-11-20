class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = 0
        end = 1
        prev_start = intervals[0][start]
        prev_end = intervals[0][end]
        index = 1
        output = []
        while index < len(intervals):
            if intervals[index][start] <= prev_end:
                prev_end = max(prev_end,intervals[index][end])
            else:
                output.append([prev_start,prev_end])
                prev_start = intervals[index][start]
                prev_end = intervals[index][end]
            index+=1
        output.append([prev_start,prev_end])
        return output                              
    
                                
                            