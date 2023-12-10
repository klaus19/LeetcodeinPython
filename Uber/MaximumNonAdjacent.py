class Solution(object):

    def max_sum_non_adjacent(self,nums):
        n = len(nums)

        # Handle base cases
        if n == 0:
            return 0
        elif n == 1:
            return max(0, nums[0])

        # Initialize the dp array
        dp = [0] * n
        dp[0] = max(0, nums[0])
        dp[1] = max(dp[0], nums[1])

        # Build the dp array using the recursive relation
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i], nums[i])

        # The final result is the maximum value in the dp array
        return max(dp)

if __name__ == '__main__':
    # Example usage:
    nums = [2, 7, 9, 3, 1]
    print("Maximum sum of non-adjacent subarray:", Solution().max_sum_non_adjacent(nums))
