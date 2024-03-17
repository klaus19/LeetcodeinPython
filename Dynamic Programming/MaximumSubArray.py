class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0

        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)
        return max(dp)

if __name__ == '__main__':
    arr = [5,4,-1,7,8]
    print(Solution().maxSubArray(arr))