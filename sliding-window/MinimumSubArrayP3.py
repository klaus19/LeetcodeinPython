class Solution(object):

    def minimumSubArray(self, array,target):

        left=0
        min_len = float("inf")
        curr_sum=0

        for right in range(len(array)):

            curr_sum+=array[right]

            while curr_sum >=target:
                min_len = min(min_len,right-left+1)
                curr_sum-=array[left]
                left+=1

        return min_len if min_len!=float("inf") else -1

