class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0

        # [rob1,rob2,n,n+1...]

        for n in nums:
            tempMax = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tempMax
        return rob2


if __name__ == "__main__":
    ltr = [1, 2, 3, 1]
    print(Solution().rob(ltr))
