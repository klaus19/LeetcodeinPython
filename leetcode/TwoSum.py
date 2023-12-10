class Solution(object):
    def twoSum(self, nums, target):

        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return

if __name__ == '__main__':
    nums =[3,4,6,8]
    target = 10
    print(Solution().twoSum(nums, target))