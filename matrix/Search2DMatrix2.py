from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        i = ROWS-1
        j = 0

        while i >= 0 and j < COLS:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                 i -= 1
            else:
                j += 1
        return False

if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target=5
    print(Solution().searchMatrix(matrix,target))