class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], idx]
            else:
                num_map[num] = idx

if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    result = Solution().twoSum(nums, target)
    print(result)
