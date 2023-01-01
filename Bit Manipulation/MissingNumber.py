from typing import List


class Solution(object):

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)


if __name__ == "__main__":
    pt = [0, 1, 3]
    print(Solution().missingNumber(pt))
