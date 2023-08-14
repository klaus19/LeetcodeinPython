class Solution(object):

    def maximumSubArray(self,nums,target):

        left=0
        min_length= float("inf")
        curr_summ=0

        for right in range(len(nums)):
            curr_summ +=nums[right]

            while curr_summ >= target:

                min_length = min(min_length,right-left+1)
                curr_summ -=nums[left]
                left+=1

        return min_length if min_length != float('inf') else -1


if __name__ == '__main__':
    arr = [2,3,1,2,4,3]
    target=7
    print(Solution().maximumSubArray(arr,target))

