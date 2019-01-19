# Python3 program to print
# given matrix in spiral form
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Steps:
    1) Move right with row 0 and increment col
    2) increment row_start

    3) Move down with col = end and increment row
    4) decrement col_end

    5) Check if row_start<=row_end ****
    6) Move left and decrement row
    7) decrement row_end


    8) Check if col_start<=col_end ****
    9) Move right and increment row_start
    10) increment col_start

'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return matrix


        result = []

        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        row_start = 0
        row_end   = rows
        row_pointer = 0

        col_start = 0
        col_end   = cols
        col_pointer = 0

        while(row_start <= row_end and col_start <= col_end):
            # print first row
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])

            row_start += 1

            # print last col
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])

            col_end -= 1

            # print last row
            if row_start <= row_end: # Tip check this to avoid overlap
                for j in range(col_end, col_start-1, -1):
                    result.append(matrix[row_end][j])

            row_end -= 1

            # print first col
            if col_start <= col_end: # Tip check this to avoid overlap
                for i in range(row_end, row_start-1, -1):
                    result.append(matrix[i][col_start])

            col_start += 1


        return result


if __name__=='__main__':
    sol = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    actual_result = sol.spiralOrder(matrix)
    expected_result = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert actual_result == expected_result