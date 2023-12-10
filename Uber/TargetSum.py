class Solution(object):
    def targetSum(self,nums,target):
        dp = {}

        def backtrack(i,total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i,total) in dp:
                return dp[(i,total)]

            dp[(i,total)] = (backtrack(i+1,total+nums[i])+
                             backtrack(i+1,total-nums[i]))
            return dp[(i,total)]
        return backtrack(0,0)

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    print(Solution().targetSum(nums,target))