class Solution(object):
    def findMin(self, nums):

        mini_value = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < mini_value:
                mini_value = nums[i]

        return mini_value


if __name__ == "__main__":
    lt = [3, 4, 5, 1, 2]
    print(Solution().findMin(lt))
