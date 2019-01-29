'''
280. Wiggle Sort
Medium

344

42

Favorite

Share
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

'''


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return

        wave = True

        for i in range(len(nums)-1):
            if wave:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]  # swap
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]  # swap

            wave = not wave # toggle value to create value


        return nums


if __name__=='__main__':
    sol = Solution()
    nums = [3,5,2,1,6,4]
    actual_result = sol.wiggleSort(nums)
    expected_result = [3,5,1,6,2,4]
    assert actual_result == expected_result