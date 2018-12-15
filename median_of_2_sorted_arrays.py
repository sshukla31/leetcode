'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

'''
Solution:
    Time complexity is O(log(min(x,y))
    Space complexity is O(1)

    Refer:
    https://github.com/mission-peace/interview/blob/master/src/com/interview/binarysearch/MedianOfTwoSortedArrayOfDifferentLength.java
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation/4

'''

import sys

MIN_INT = -sys.maxint - 1
MAX_INT = sys.maxint

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        # must have code starts here
        len_x = len(nums1)
        len_y = len(nums2)

        if len_x > len_y:
            # Tip1: swap arrays to keep left array always small
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = len_x

        while(low <= high):
            partition_x = (low + high)/2
            partition_y = (len_x + len_y + 1)/2 - partition_x  # Tip2: how to calculate partition of large array

            #print nums1[:partition_x]
            #print nums1[partition_x:]
            #print nums2[:partition_y]
            #print nums2[partition_y:]

            # Find comparable elements of both arrays
            # Tip 3: if left side is empty use MIN_INT and if right is empty then MAX_INT
            x_left_partition_max = MIN_INT if partition_x == 0 else nums1[partition_x - 1]
            x_right_partition_min = MAX_INT if partition_x == len_x else nums1[partition_x]

            y_left_partition_max = MIN_INT if partition_y == 0 else nums2[partition_y - 1]
            y_right_partition_min = MAX_INT if partition_y == len_y else nums2[partition_y]

            if all([
                x_left_partition_max <= y_right_partition_min,
                y_left_partition_max <= x_right_partition_min
            ]):
                if (len_x + len_y) % 2 == 0:
                    return 0.5 * (
                        max(x_left_partition_max, y_left_partition_max) +
                        min(x_right_partition_min, y_right_partition_min)
                    )
                else:
                    return max(
                        x_left_partition_max, y_left_partition_max
                    )
            elif x_left_partition_max > y_right_partition_min:
                # Tip4: update high pointer if x is greater
                high = partition_x - 1
            else:
                # Tip5: update low pointer if x right min is lower
                low = partition_x + 1

if __name__=='__main__':

    solution = Solution()
    list_1 = [1, 3, 8, 9, 15]
    list_2 = [7, 11, 18, 19, 21, 25]
    expected_result = 11
    actual_result = solution.findMedianSortedArrays(list_1, list_2)
    assert expected_result == actual_result

    list_1 = [23, 26, 31, 35]
    list_2 = [3, 5, 7, 9, 11, 16]
    expected_result = 13.5
    actual_result = solution.findMedianSortedArrays(list_1, list_2)
    assert expected_result == actual_result
