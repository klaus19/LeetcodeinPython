
class Solution(object):
    def maximumSubArray(self,nums):

        curr_sum = nums[0]
        max_sum = curr_sum

        for i in range(1,len(nums)):
            curr_sum = max(curr_sum+nums[i],nums[i])
            max_sum = max(curr_sum,max_sum)

        return max_sum

if __name__ == '__main__':
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(Solution().maximumSubArray(nums))