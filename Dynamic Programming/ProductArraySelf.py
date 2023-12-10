class Solution(object):
    def findUnsortedSubarray(self, nums):

        n = len(nums)
        right = [1]*n
        left = [1]*n
        output = [1]*n

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]

        for i in range(n):
            output[i] = right[i]*left[i]

        return output

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().findUnsortedSubarray(nums))
