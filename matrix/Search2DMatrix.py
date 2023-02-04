class Solution(object):

    def searchMatrix(self, matrix, target):
        # Base condition...
        if not matrix:
            return False
        row = len(matrix)  # Number of Rows of the matrix...
        col = len(matrix[0])  # Number of Columns of the matrix...
        # Initialize beg index of the considered 1D matrix (i.e: 0)...
        beg = 0
        # Set end index of the considered 1D matrix (i.e: row*col)...
        end = row * col
        # Now apply binary search & Run a while loop...
        while beg < end:
            # Get the middle index as (beg + (end - beg)) // 2...
            mid = beg + (end - beg) // 2
            # Set the element at middle index using matrix[mid / col][mid % col].
            idx = matrix[mid // col][mid % col];
            # If the element present at the middle index is equal to the target integer, return true...
            if idx == target:
                return True
            # If the middle index element is lesser than the target...
            if idx < target:
                beg = mid + 1
            # If the middle index is greater than the target...
            else:
                end = mid
        return False  # As we didn't get the target, we can directly return false...



if __name__ == '__main__':

    lt = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target =3
    print(Solution().searchMatrix(lt,target))




