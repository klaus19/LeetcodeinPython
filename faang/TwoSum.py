class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums:
                try:
                    j = nums.index(another)
                    if i != j:
                        return [i, j]
                except ValueError as e:
                    # There has no item in list
                    continue
        return []


if __name__ == "__main__":
    l = [2, 7, 8, 11]
    t = 9
    print(Solution().twoSum(l, t))
