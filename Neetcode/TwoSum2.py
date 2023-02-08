class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1
            # binary search
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] + nums[i] == target:
                return [i + 1, left + 1]