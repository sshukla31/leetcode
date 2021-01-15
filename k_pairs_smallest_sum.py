'''
373. Find K Pairs with Smallest Sums
Medium

1724

118

Add to List

Share
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''


import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        '''
        if not nums1 or not nums2:
            return []

        heap = []
        result = []
        visited = [(0, 0)]

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while len(result) < k and heap:
            val = heapq.heappop(heap)
            result.append(
                [nums1[val[1]], nums2[val[2]]]
            )

            if val[1] + 1 < len(nums1) and (val[1]+1, val[2]) not in visited:
                heapq.heappush(
                    heap,
                    (nums1[val[1] + 1] + nums2[val[2]], val[1]+1, val[2])
                )
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heapq.heappush(
                    heap,
                    (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1)
                )
                visited.append((val[1], val[2] + 1))



        return result



if __name__ == '__main__':
    sol = Solution()

    # Test Case 1:
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    expected_result = [[1,2],[1,4],[1,6]]
    actual_result = sol.kSmallestPairs(nums1, nums2, k)
    assert expected_result == actual_result

    # Test Case 2:
    nums1 = []
    nums2 = []
    k = 5
    expected_result = []
    actual_result = sol.kSmallestPairs(nums1, nums2, k)
    assert expected_result == actual_result

    # Test Case 3:
    nums1 = []
    nums2 = [2,4,6]
    k = 5
    expected_result = []
    actual_result = sol.kSmallestPairs(nums1, nums2, k)
    assert expected_result == actual_result

    # Test Case 4:
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 2
    expected_result = [[1,2],[1,4]]
    actual_result = sol.kSmallestPairs(nums1, nums2, k)
    assert expected_result == actual_result



