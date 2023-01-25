class Solution(object):

    def findMin(self, nums):

        left,right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    lt = [3,4,5,1,2]
    print(Solution().findMin(lt))
