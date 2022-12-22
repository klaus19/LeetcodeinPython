class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i


if __name__ == "__main__":
    lt = [4, 5, 6, 7, 0, 1, 2]
    t1 = 0

print(Solution().search(lt,t1))
