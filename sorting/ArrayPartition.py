class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        max_sum = 0

        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum

if __name__ == '__main__':
    nums = [1,4,3,2]
    print(Solution().arrayPairSum(nums))