'''

215. Kth Largest Element in an Array
Medium
1460
141


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4



2 sol:
    1) using Heap (min heap)
    2) Using quick select   Reference:
       https://rcoh.me/posts/linear-time-median-finding/

* Note: quick_select can be used to find median of unsorted array. We need to pass
        Even elements:
          quick_select(l, k=len(l)/2)
        Odd elements:
         0/5 * (quick_select(l, k=len(l)/2) + quick_select(l, k=len(l)/2 -1 ))

'''

import random
from Queue import PriorityQueue

class Solution(object):
    def find_Kth_largest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        pq = PriorityQueue()

        for num in nums:
            pq.put(num)
            if pq.qsize() > k:
                pq.get()

        return None if pq.empty() else pq.get()


    def quick_select(self, l, k, pivot_func=random.choice):
        if len(l) == 1:
            # optimization
            assert k == 0
            return l[0]

        pivot = pivot_func(l)
        lows = []
        highs = []
        pivots = []

        for num in l:
            if num < pivot:
                lows.append(num)
            elif num > pivot:
                highs.append(num)
            else:
                pivots.append(num)


        if k < len(lows):
            return self.quick_select(lows, k)
        elif k < len(lows) + len(pivots):
            # We got lucky and guessed the median
            return pivots[0]
        else:
            return self.quick_select(highs, k - len(lows) - len(pivots))


if __name__=='__main__':

    # Applying solution 1
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    actual_result = sol.find_Kth_largest(nums, k)
    expected_result = 5
    assert actual_result == expected_result

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    actual_result = sol.find_Kth_largest(nums, k)
    expected_result = 4

    # Applying solution 2
    nums = [3,2,1,5,6,4]
    k = 2
    actual_result = sol.quick_select(nums, len(nums) - k)
    expected_result = 5
    assert actual_result == expected_result

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    actual_result = sol.quick_select(nums, len(nums) - k)
    expected_result = 4
    assert actual_result == expected_result
