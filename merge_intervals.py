'''
56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Steps:
    1) Sort based on start
    2) If start is within the range of last stored element in result, update the
       last result end value
    3) If start is out of range, append to result to create new element
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1 or intervals is None:
            return intervals

        result = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if result and interval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(interval)

        return result


if __name__=='__main__':
    sol = Solution()
    intervals = [ Interval(interval[0], interval[1]) for interval in [ [1,3] ,[2,6], [8,10], [15,18]] ]
    expected_result = [Interval(interval[0], interval[1]) for interval in [1,6],[8,10],[15,18]]
    actual_result = sol.merge(intervals)
    print actual_result
    print expected_result