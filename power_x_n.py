'''

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        if n < 0:
            n = abs(n)
            x = 1/x

        temp = self.myPow(x, n/2) # divide & conquer eg: 2^4 = 2^2 * 2^2

        if n % 2 == 0:
            return temp * temp
        else:
            # when odd value of n. eg: 2^9 = 2*2^4*2^4
            return x * temp * temp



if __name__ == '__main__':
    sol = Solution()
    actual_result = sol.myPow(2.0, 10)
    expected_result = 1024.00000
    assert actual_result == expected_result


    actual_result = sol.myPow(2.10000, 3)
    expected_result = 9.26100
    assert round(actual_result, 5) == expected_result

    import ipdb; ipdb.set_trace()

    actual_result = sol.myPow(2.00000, -2)
    expected_result = 0.25
    assert actual_result == expected_result