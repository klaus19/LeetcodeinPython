class Solution(object):

    def maximum_subarray(self,nums):
        ret = float('-inf')
        prevsum = nums[0]

        for i in range(1, len(nums)):
            prevsum = max(nums[i], nums[i] + prevsum)
            ret = max(ret, prevsum)

        ret = max(nums[0], ret)

        return ret

if __name__ == '__main__':

    st = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maximum_subarray(st))