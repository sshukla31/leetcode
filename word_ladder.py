'''
127. Word Ladder
Medium

4168

1358

Add to List

Share
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''



try:
   import queue
except ImportError:
   import Queue as queue

from string import ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wl = set(wordList)

        if endWord not in wl:
            return 0


        qu = queue.Queue()
        qu.put((beginWord, 1))

        while queue:
            curr, length = qu.get()

            if curr == endWord:
                return length


            for index in range(len(curr)):
                # for char in range(ord('a'), ord('z')+1):
                temp = curr
                for char in ascii_lowercase:
                    if char == temp[index]:
                        continue

                    temp = temp[:index] + char + temp[index+1:]
                    if temp == endWord:
                            return length+1

                    if temp in wl:
                        qu.put((temp, length+1))
                        wl.remove(temp)



        return depth



if __name__=='__main__':
    sol = Solution()


    # Test Case: 1
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    expected_value =  5
    actual_value = sol.ladderLength(beginWord, endWord, wordList)
    assert actual_value == expected_value


    # Test Case: 2
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    expected_value =  0
    actual_value = sol.ladderLength(beginWord, endWord, wordList)
    assert actual_value == expected_value

