'''

79. Word Search
Medium

4862

214

Add to List

Share
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
------------------
 Ax | Bx | Cx | E |
------------------
 S  | F  | Cx | S |
------------------
 A  | Dx | Cx | E |
------------------
*NOTE: i have marked 'x' with characters denoting the path and word found pattern

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

----------------
 A | B | C | E |
----------------
 S | F | C | Sx|
----------------
 A | D | Ex| Ex|
----------------

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 200
1 <= word.length <= 103
board and word consists only of lowercase and uppercase English letters.
'''




class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """


        self.ROWS = len(board)
        self.COLS = len(board[0])

        self.board = board


        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    # match found
                    return True

        # no match found
        return False


    def backtrack(self, row, col, suffix):
        # as we reached the end of suffix and nothing left to search
        # hence, we have reached bottom case
        if len(suffix) == 0:
            return True

        # Check boundary and matching value
        if (
            row < 0 or
            row == self.ROWS or
            col < 0 or
            col == self.COLS or
            self.board[row][col] != suffix[0]
        ):
            return False


        self.board[row][col] = "-1"
        ret = False

        for row_offset, col_offset in [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]:
            ret = self.backtrack(row + row_offset, col + col_offset, suffix[1:])

            if ret:
                break


        self.board[row][col] = suffix[0]

        return ret


sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

# Test 1
word = "ABCCED"
assert True == sol.exist(board, word)


# Test 2
word = "SEE"
assert True == sol.exist(board, word)


# Test 3
word = "ABCB"
assert False == sol.exist(board, word)
