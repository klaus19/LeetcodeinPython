class Solution(object):

    def searchMatrix(self,matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                left, right = 0, n - 1
                while left <= right:
                    mid2 = left + (right - left) // 2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        left = mid2 + 1
                    else:
                        right = mid2 - 1
                return False
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':

    lt = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target =3
    print(Solution().searchMatrix(lt,target))




