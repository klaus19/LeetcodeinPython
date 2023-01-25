class Solution(object):

    def search(self, nums, target):

        left,right = 0,len(nums)-1

        if len(nums)==1 and nums[0]==target:
               return 0

        while left < right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] >target:
                right = mid-1
            else:
                left = mid+1
        return -1

if __name__ == "__main__":
    lt = [-1,0,3,5,9,12]
    target=9
    p=[5]
    t=5
    print(Solution().search(lt,target))
    print(Solution().search(p,t))