class Solution(object):

    def minimum(self,nums,target):
        if not nums: return -1

        left=0
        min_len=float("inf")
        curr_sum=0

        for right in range(len(nums)):
            curr_sum+=nums[right]

            while curr_sum>=target:

                min_len = min(min_len,right-left+1)
                curr_sum -=nums[left]
                left+=1

        return  min_len if min_len!=float("inf") else -1

