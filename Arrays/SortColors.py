class Solution(object):

    def sortColor(self,nums):
        low=0
        mid=0
        high=len(nums)-1

        while mid <= high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

#Time compelexity would O(n) as it take equal amount time to traverse

  # two pointer technique from the sliding window technique ise used

