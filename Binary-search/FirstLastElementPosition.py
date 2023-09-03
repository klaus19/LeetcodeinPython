class Solution(object):
    def searchRange(self, nums, target):
        left = self.findFirst(nums, target)
        right = self.findLast(nums, target)
        return [left, right]

    def findFirst(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid  # Update result and continue searching to the left
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return result

    def findLast(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid  # Update result and continue searching to the right
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return result

# Example usage:
# nums = [5, 7, 7, 8, 8, 8, 10]
# target = 8
# Output: [3, 5]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums,target))

# Uber, Facebook, Amazon,Google,Microsoft,Adobe,Bloomberg, TikTok