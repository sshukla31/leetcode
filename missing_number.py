'''

268. Missing Number
Easy

729

1115

Favorite

Share
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)

        for i in range(0, len(nums)):
            xor = xor ^ i ^ nums[i]

        return xor

    def missingNumberClassic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ideal_total = n*(n + 1) / 2

        total = 0
        for num in nums:
            total += num

        return ideal_total - total



if __name__=='__main__':
    nums =  [3,0,1]
    sol = Solution()
    actual_result = sol.missingNumber(nums)
    expected_result = 2
    assert actual_result == expected_result

