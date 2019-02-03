'''
46. Permutations
Medium

1604

45

Favorite

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]



1) Use Backtracking
2) Swap elements with first index of array
3) Increase the start pointer
4) Once start == end pointer add to result

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(nums, 0, len(nums), result)

        return result

    def backtrack(self, nums, start, end, result):
        if start == end:
            # ** Tip1: we do nums[:] to get elements instead of nums to avoid mutability
            result.append(nums[:])
        else:
            for index in xrange(start, end):
                nums[start], nums[index] = nums[index], nums[start]  # swap
                self.backtrack(nums, start+1, end, result)
                nums[start], nums[index] = nums[index], nums[start]  # backtrack to original value


if __name__=='__main__':
    sol = Solution()
    actual_result = sol.permute(nums=[1, 2, 3])
    expected_result = [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
    assert sorted(actual_result) == sorted(expected_result)
