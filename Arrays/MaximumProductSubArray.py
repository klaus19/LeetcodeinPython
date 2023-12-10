class Solution(object):
    def maxProduct(self, nums):

        curr_max = nums[0]
        final_max = curr_max

        for i in range(1,len(nums)):
            curr_max = max(nums[i]*curr_max,nums[i],curr_max)
            final_max = max(curr_max,final_max)

        return final_max

if __name__ == '__main__':
    nums =[2,3,-2,4]
    print(Solution().maxProduct(nums))