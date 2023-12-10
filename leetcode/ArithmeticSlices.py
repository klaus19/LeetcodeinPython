class Solution(object):
    def noArithmetic(self,nums):
        curr=0
        count=0

        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr+=1
                count+=curr
            else:
                curr=0
        return count

if __name__ == '__main__':
    nums =[1,2,3,4]
    print(Solution().noArithmetic(nums))