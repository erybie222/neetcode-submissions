"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
        
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [[intervals[0]]]
        isAdded = False
        for i in range(1,len(intervals)):
            isAdded = False
            for room in rooms:
                if room[-1].end <= intervals[i].start:
                    room.append(intervals[i])
                    if room[-2].end > room[-1].end:
                        room[-2], room[-1] = room[-1], room[-2]
                    isAdded = True
                    break
            if not isAdded:
                rooms.append([intervals[i]])
        return len(rooms)
