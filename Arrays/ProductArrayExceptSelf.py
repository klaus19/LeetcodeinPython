class Solution(object):

    def product_except(self,arr):
        res = [1] * len(arr)

        prefix=1
        for i in range(len(arr)):
            res[i]=prefix
            prefix *=arr[i]
        postfix=1
        for i in range(len(arr),1,-1):
            res[i] *= postfix
            postfix *= arr[i]
        return res

if __name__ == "__main__":
    lt = [2,3,4]
    print(Solution().product_except(lt))