class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])
        
        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1], intervals[i] = [], [intervals[i-1][0], max(intervals[i-1][1],intervals[i][1])]
                
        for _ in range(intervals.count([])):
            intervals.remove([])
            
        return intervals
