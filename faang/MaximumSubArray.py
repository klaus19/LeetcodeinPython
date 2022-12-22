class Solution(object):

    def maximum_subarray(self, nums):

        n = len(nums)
        curr_sum = 0
        max_sum = -1e8

        for i in range(0, n):
            curr_sum = curr_sum + nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum

            elif curr_sum < 0:
                curr_sum = 0

        return max_sum


if __name__ == "__main__":
    l1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maximum_subarray(l1))
