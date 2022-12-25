class Solution(object):

    def rob(self, nums):
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
            rob1, rob2 = 0, 0

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2


if __name__ == "__main__":
    pt = [2, 3, 2]
    print(Solution().rob(pt))
