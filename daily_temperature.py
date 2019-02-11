'''
739. Daily Temperatures
Medium

963

27

Favorite

Share
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of T and WW is the number of allowed values for T[i]. Each index gets pushed and popped at most once from the stack.

Space Complexity: O(W)O(W). The size of the stack is bounded as it represents strictly increasing temperatures.


Solution:
1) Create stack containing T's index value
2) Traverse T in reverse order. Why ?? Because the current date looks for future value.
   Hence, we go reverse and keep in stack and then use current val to compare against last stack val
2) If the last T[stack[-1]] < T[i], this means the current top stack value won't help and we go next
   for bigger or say higher temperate to find diff. We keep index value in stack as it depicts each day
3) We keep popping the value until a bigger value is found
4) We then use a result array, result[i] = stack[-1] - i // current day - future day diff
5) return result

'''


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        if T is None or len(T) == 0:
            return

        len_T = len(T)
        result = [0] * len_T

        # indexes from high temp to low temp
        # If we encounter low temp on top than current pop out
        stack = []


        for i in range(len(T) - 1, -1, -1):
            while(stack) and T[i] >= T[stack[-1]]:
                stack.pop()


            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result


if __name__ == '__main__':
    sol = Solution()
    T = [73,74,75,71,69,72,76,73]
    expected_result = [1,1,4,2,1,1,0,0]
    actual_result = sol.dailyTemperatures(T)

    assert actual_result == expected_result