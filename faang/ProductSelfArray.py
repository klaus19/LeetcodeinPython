class Solution(object):

    def productExceptSelf(self, nums):

        res = [1]
        prev = 1
        # scan forward
        for i in range(1, len(nums)):
            prev = prev * nums[i - 1]
            res.append(prev)
        # scan backward
        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            prev = prev * nums[i + 1]
            res[i] = res[i] * prev

        return res


if __name__ == "__main__":
    ltr = [1, 2, 3, 4]
    print(Solution().productExceptSelf(ltr))
