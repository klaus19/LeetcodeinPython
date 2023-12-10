class Solution(object):

    def find_max_value(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        max_value = matrix[0][0]
        max_row = max_cols =0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] > max_value:
                    max_value = matrix[i][j]
                    max_row = i
                    max_cols = j

        return max_value,max_row,max_cols

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


    print(Solution().find_max_value(matrix))