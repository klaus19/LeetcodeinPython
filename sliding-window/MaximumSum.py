class Solution(object):

    # [100, 200, 300, 400] k=2

    def maximumSum(self,arr,k):

        n=len(arr)
        if k>n:
            return -1

        if len(arr)<k:return -1

        maxSum =sum(arr[:k])

        curr_sum=maxSum

        for i in range(k,n):
            curr_sum = curr_sum -arr[i-k]-arr[i]
            maxSum = max(maxSum,curr_sum)

        return maxSum


if __name__ == '__main__':
    aa = [2, 1, 5, 1, 3, 2]
    k=3
    print(Solution().maximumSum(aa,k))

