class Solution(object):

    def searchRange(self, nums, target):

       lo=0
       hi=len(nums)

       while lo < hi:
           mid = lo+(hi - lo)//2

           if nums[mid]==target:
               return mid
           elif nums[mid] >target:
               hi = mid-1

           elif nums[mid] < target:
               lo = mid + 1

           return mid


if __name__ == "__main__":
    lt = [5,7,7,8,8,10]
    t = 7
    print(Solution().searchRange(lt, t))
