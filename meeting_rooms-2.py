'''
253. Meeting Rooms II
Medium

1018

20

Favorite

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

steps:
    1) sort intervals based on start time
    2) use MIN HEAP to insert first element's end time and set room_count = 1
       MIN HEAP will have smallest end time meeting room available on top which can
       be occupied by next meeting interval
    3) for subsequent intervals,
         if new_interval.start < min_heap.end_time # means overlap:
             increment room_count and also add in heap
        else:
            # there is no overlap
            pop the top element from heap and add new_interval
            Hence, we don't need new meeting room

'''


from Queue import PriorityQueue

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "{}-{}".format(self.start, self.end)


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        if len(intervals) == 1:
            return 1

        pq = PriorityQueue()
        intervals = sorted(intervals, key=lambda x: x.start)  # sort based on start time
        room_count = 1

        pq.put(intervals[0].end)  # insert end time

        for interval in intervals[1:]:  # start from second element as we have pushed first
            if interval.start < pq.queue[0]:
                room_count += 1
                pq.put(interval.end)
            else:
                pq.get()  # pop out the first element as meeting is over
                pq.put(interval.end)

        return room_count


if __name__=='__main__':
    sol = Solution()
    intervals = [ Interval(interval[0], interval[1]) for interval in [ [0,30] ,[5,10], [15,20]] ]
    expected_result = 2
    actual_result = sol.minMeetingRooms(intervals)
    assert expected_result == actual_result



    intervals = [ Interval(interval[0], interval[1]) for interval in [ [7, 10] ,[2, 4]] ]
    expected_result = 1
    actual_result = sol.minMeetingRooms(intervals)
    assert expected_result == actual_result

