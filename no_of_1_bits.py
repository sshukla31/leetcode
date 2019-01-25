'''
191. Number of 1 Bits
Easy

355

329

Favorite

Share
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        result = 0
        while(n!=0):
            result = result + (n&1)
            n = n >> 1

        return result



if __name__=='__main__':
    sol = Solution()
    actual_result = sol.hammingWeight(3)
    expected_result = 2


    actual_result = sol.hammingWeight(5)
    expected_result = 2
    assert actual_result == expected_result

    actual_result = sol.hammingWeight(11)
    expected_result = 3
    assert actual_result == expected_result
