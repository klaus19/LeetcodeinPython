class Solution(object):

    def max_sub_array(self,arr):
        curr_sum=arr[0]
        max_sum=arr[0]

        for i in range(1,len(arr)):
            curr_sum = max(arr[i],curr_sum+arr[i])
            max_sum = max(curr_sum,max_sum)
        return max_sum

if __name__ == '__main__':
    p = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().max_sub_array(p))