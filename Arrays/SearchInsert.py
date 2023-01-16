from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target=3
    lt =[1,3,5,6]
    t = 2
    print(Solution().searchInsert(arr,target))
    print(Solution().searchInsert(lt,t))