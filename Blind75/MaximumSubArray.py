class Solution(object):

    def maximum_subarray(self,nums):

        prev_sum = nums[0]
        max_sum = float('-inf')
        for i in range(1, len(nums)):
            prev_sum = max(nums[i], nums[i] + prev_sum)
            max_sum = max(max_sum, prev_sum)

        max_sum = max(nums[0], max_sum)

        return max_sum

if __name__ == '__main__':

    st = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maximum_subarray(st))