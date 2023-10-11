class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        if not nums:
            return None
        ans=1
        for i in range(len(nums)):
            if nums[i] == ans:
                ans+=1

        return ans

if __name__ == '__main__':
    nums = [3,4,-1,1]
    print(Solution().firstMissingPositive(nums))