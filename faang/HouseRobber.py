class Solution(object):
    def rob(self, nums):

        if not nums: return 0

        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i - 1 > 0:
                dp[i] = nums[i] + max(dp[:i - 1])
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == "__main__":
    ltr = [1, 2, 3, 1]
    print(Solution().rob(ltr))
