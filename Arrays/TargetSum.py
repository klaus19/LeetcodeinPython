class Solution(object):

    def target(self,nums,target):

        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = lo+(hi-lo)//2

            if nums[mid]==target:
                return mid
            elif nums[mid] <target:
                lo = mid+1

            else:
                hi = mid-1

        return -1

if __name__ == '__main__':
    arr = [1,2,3,5]
    target =5
    print(Solution().target(arr, target))

