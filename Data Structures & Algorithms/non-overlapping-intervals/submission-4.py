class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        counter = 0
        
        for i in range(len(intervals) -1):
            if intervals[i][1] <= intervals[i+1][0]:
                continue
            else:
                counter += 1
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i+1] = intervals[i]

        return counter

