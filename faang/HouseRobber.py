class Solution(object):
    def rob(self, nums):

        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        sums = [0] * n
        sums[0] = nums[0]
        sums[1] = max(nums[0], nums[1])

        for i in range(2, n):
            sums[i] = max(sums[i - 2] + nums[i], sums[i - 1])

        return sums[n - 1]


if __name__ == "__main__":
    ltr = [1, 2, 3, 1]
    print(Solution().rob(ltr))
