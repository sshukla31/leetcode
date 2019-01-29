'''
17. Letter Combinations of a Phone Number
Medium

1774

249

Favorite

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


self.phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Solution:
1) use Backtracking



Complexity Analysis

Time complexity : \mathcal{O}(3^N \times 4^M)O(3
N
 ×4
M
 ) where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.

Space complexity : \mathcal{O}(3^N \times 4^M)O(3
N
 ×4
M
 ) since one has to keep 3^N \times 4^M3
N
 ×4
M
 solutions.

'''



class Solution(object):

    def __init__(self):
        self.phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        len_digits = len(digits)
        if len_digits == 0:
            return []
        elif len_digits == 1:
            return self.phone[digits[0]]
        else:
            result = []
            combination = ""
            return self.backtrack(digits, combination, result)


    def backtrack(self, digits, combination, result):
        if len(digits) == 0:
            result.append(combination)
        else:
            for char in self.phone[digits[0]]:
                self.backtrack(digits[1:], combination+char, result)



        return result