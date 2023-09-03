class Solution(object):
    def search(self, nums, target):
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            mid = lo + (hi-lo)//2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                 hi = mid-1
            else:
                 lo = mid+1

            return mid

if __name__ == '__main__':
    nums = [4,5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums,target))

