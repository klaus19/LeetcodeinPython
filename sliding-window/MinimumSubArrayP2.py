class Solution(object):

    def minimumSubArray(self,arr,target):

        left=0
        min_length = float("inf")
        curr_sum=0

        for right in range(len(arr)):

            curr_sum +=arr[right]

            while curr_sum>=target:
                min_length = min(min_length,right-left+1)
                curr_sum -=arr[left]
                left +=1

        return  min_length if min_length!=float("inf") else -1


if __name__=='__main__':
    arr = [5,6,7]
    target = 11
    print(Solution().minimumSubArray(arr,target))



# t.c IS O(n)