'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return -1

        if len(s) == 1:
            return 0


        result = -1
        char_dict = defaultdict(int)

        for char in s:
            char_dict[char] += 1

        for index, char in enumerate(s):
            if char_dict[char] == 1:
                result = index
                break
