class Solution(object):
    def findDuplicate(self, nums):
        num_set = set()

        for i in range(len(nums)):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                return nums[i]

if __name__ == '__main__':
    arr = [1, 3, 2, 2]
    duplicate = Solution().findDuplicate(arr)
    print(duplicate)
