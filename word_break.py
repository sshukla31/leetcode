'''
139. Word Break
Medium

5675

269

Add to List

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false



Reference:
 1) Tushar Roy
    https://www.youtube.com/watch?v=WepWFGxiwRs&ab_channel=TusharRoy-CodingMadeSimple
'''




class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """



        '''
            * Dynamic programming version for breaking word problem.
            * It returns null string if string cannot be broken into multipe words
            * such that each word is in dictionary.
            * Gives preference to longer words over splits
            * e.g peanutbutter with dict{pea nut butter peanut} it would result in
            * peanut butter instead of pea nut butter.
        '''

        wdict = set(wordDict)
        word = s
        word_len = len(word)




        T = [ [-1]*word_len for i in range(word_len)]   # -1 indicates string between i to j cannot be split

        # fill up the matrix in bottom up manner
        for l in range(1, word_len+1):            # l = 1(ie, select 1 char), l = 2(select 2 char),l=n(select n char)
            for i in range(0, (word_len-l + 1)):  # (word_len-l + 1)-> selects no of character based on size of l
                j = i + l-1
                _str = word[i: j+1]

                # if string between i to j is in dictionary T[i][j] is true
                if _str in wdict:
                    T[i][j] = i
                    continue

                # find a k between i+1 to j such that T[i][k-1] && T[k][j] are both true
                for k in range(i+1, j+1):
                    if(T[i][k-1] != -1 and T[k][j] != -1):
                        T[i][j] = k
                        break




        if(T[0][word_len -1] == -1):
            return None


        # create space separate word from string is possible
        buffer = ""
        i = 0;
        j = word_len -1;
        while(i <= j):
            k = T[i][j];
            if(i == k):
                buffer+=word[i: j+1]
                break;

            buffer+=word[i: k] + " "
            i = k


        return buffer




if __name__=='__main__':
    sol = Solution()


    # Test Case: 1   :  happy case
    s = "leetcode"
    wordDict = ["leet", "code"]
    actual_result = True if sol.wordBreak(s, wordDict) else False
    expected_result = True
    assert actual_result == expected_result


    # Test Case: 2   : happy case: corner case: single character
    s = "a"
    wordDict = ["a"]
    actual_result = True if sol.wordBreak(s, wordDict) else False
    expected_result = True
    assert actual_result == expected_result


    # Test Case: 3  : happy case
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    actual_result = True if sol.wordBreak(s, wordDict) else False
    expected_result = True
    assert actual_result == expected_result


    # Test Case: 4 : unhappy case
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    actual_result = True if sol.wordBreak(s, wordDict) else False
    expected_result = False
    assert actual_result == expected_result

