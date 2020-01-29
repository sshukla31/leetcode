'''

973. K Closest Points to Origin
Medium

1020

87

Add to List

Share
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

'''



from Queue import PriorityQueue

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """


        max_heap = PriorityQueue()
        result = []


        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]

            # we save as -distance for make minHeap as maxHeap as by default the PQ is minHeap
            max_heap.put((-distance, [point[0], point[1]]))
            if max_heap.qsize() > K:
                max_heap.get()



        while(not max_heap.empty()):
            result.append(max_heap.get()[1])

        return result





sol = Solution()

# TestCase 1
ints = [[3,3],[5,-1],[-2,4]]
K = 2
actual_output = sol.kClosest(ints, K)
expected_output = [[-2,4], [3,3]]
assert expected_output == actual_output


# TestCase 2
ints = [[1,3],[-2,2]]
K = 1
actual_output = sol.kClosest(ints, K)
expected_output = [[-2,2]]
assert expected_output == actual_output
