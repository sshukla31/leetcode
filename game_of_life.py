'''
289. Game of Life
Medium

683

142

Favorite

Share
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''


class Solution(object):

    def get_live_neighbors(self, board, rows, cols, row, col):
        lives = 0

        # note we do row+2 or col+2 as xrange returns one less index
        # eg: xrange(0, 4) = [0, 1, 2, 3]
        # As we need 8 cells around the current cell we do -1 and +1 lookup
        # we have used max() and min() to avoid validation check for outofbound
        # index check in case we have board[0][1] or board [0][3] and so on..
        for sub_row in range(max(row-1, 0), min(row+2, rows)):
            for sub_col in range(max(col-1, 0), min(col+2, cols)):
                # here we only check the first bit to see its status.
                # eg: 00 & 1 = 0 (dead) and 01 & 1 = 1 (live)
                # reason we do this and simply not check for 1 or 0 is to make sure
                # we update values at one go, instead gradually. This is one of the corner
                # case. Idea is not update until all values are read. Hence, we work with bits
                lives += board[sub_row][sub_col] & 1

        # Exclude itself to count lives count. This is super important
        lives -= board[row][col] & 1  # ???? Why do i need this ????

        return lives

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return

        rows = len(board)
        cols = len(board[0])

        for row in xrange(rows):
            for col in xrange(cols):
                live_neighbors = self.get_live_neighbors(board, rows, cols, row, col)

                if board[row][col] == 1 and live_neighbors >=2 and live_neighbors <=3:
                    # we only affect 2nd bit. now 01 becomes 11. 1st bit is old state and 2nd bit is new state
                    board[row][col] = 3

                if board[row][col] == 0 and live_neighbors == 3:
                    # make 00 to 10. where first bit was dead and now 2nd bit is live
                    board[row][col] = 2


        # Once we have read everything, now updated at once
        for row in xrange(rows):
            for col in xrange(cols):
                board[row][col] = board[row][col] >> 1


        return board


if __name__=='__main__':
    sol = Solution()
    board1 = [
	[0,1,0],
	[0,0,1],
	[1,1,1],
	[0,0,0]
    ]
    actual_output = sol.gameOfLife(board1)
    expected_output = [
	[0,0,0],
	[1,0,1],
	[0,1,1],
	[0,1,0]
    ]

    assert actual_output == expected_output