'''
22. Generate Parentheses
Medium


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


Steps: Using backtracking
https://www.youtube.com/watch?v=sz1qaKt0KGQ  - Check how backtracking works

Basically we create a Tree with recursion

Here we follow,
1) Recursion
2) Apply Constraints eg: close won't be applied unless open is applied. close will be always les than open
3) Goal (Stop Condition), when the count is met. eg: When str_len==6 , we stop

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        self.backtrack(result,"", 0, 0, n)

        return result

    def backtrack(self, result, _str, _open, _close, total):
        if len(_str) == total * 2:
            return result.append(_str)


        if _open < total:
            self.backtrack(result, _str+"(", _open+1, _close, total)

        if _close < _open:
            self.backtrack(result, _str+")", _open, _close+1, total)





if __name__=='__main__':
    sol = Solution()
    actual_result = sol.generateParenthesis(n=3)
    expected_result = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    assert actual_result == expected_result

