class Solution(object):
    def runningSum(self, nums):

        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        return nums

if __name__ == "__main__":
    pt =[1,2,3,4]
    print(Solution().runningSum(pt))