class Solution(object):
    def validMountainArray(self, arr):

        n=len(arr)
        j=1
        k = n // 2

        if len(arr) <=2:
            return False

        for i in range(1,n-1):
                while j<= n//2-1 and k!=n-1:
                    if arr[j-1] > arr[j] and arr[k+1] > arr[k]:
                        return True
                    else:
                        return False


if __name__ == '__main__':
     arr = [0,2,3,4,5,2,1,0]
     print(Solution().validMountainArray(arr))



