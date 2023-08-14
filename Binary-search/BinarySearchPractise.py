

class Solution(object):

    def binarySearch(self,nums,target):

        if target not in nums:
            return -1

        left=0
        right = len(nums)-1

        while left < right:
            mid = (left+right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1

            else:
                left = mid+1
        if nums[left] ==target: return left


if __name__ == '__main__':
    nums = [2,3,5,6,8]
    target = 7

    print(Solution().binarySearch(nums,target))


