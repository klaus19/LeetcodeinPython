class Solution(object):

    def runnerUp(self,nums):

        nums.sort()
        n = len(nums)
        max_num = nums[n-1]
        runner_up = max_num

        for i in range(n-1,-1,-1):
            if nums[i]<max_num:
                runner_up = nums[i]
            else:
                continue
        return runner_up

if __name__ == '__main__':
    nums = [3,3,1,2]
    print(Solution().runnerUp(nums))
