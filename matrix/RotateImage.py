
from typing import List

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #Transpose the matrix
        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]

        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

if __name__ == '__main__':
    lt =[[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().rotate(lt))
