from collections import Counter


class Solution(object):
    def isMajorityElement(self, nums, target):

        dict = Counter(nums)
        n = len(nums)

        if dict[target]> n//2:
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [2,4,5,5,5,5,5,6,6]
    target = 5
    print(Solution().isMajorityElement(nums, target))