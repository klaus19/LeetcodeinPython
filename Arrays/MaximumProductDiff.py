class Solution(object):
    def maximumP(self,nums):

        nums.sort()
        n = len(nums)
        for i in range (n):
            smallest = nums[0]*nums[1]
            largest = nums[n-1]*nums[n-2]

        return largest-smallest

if __name__ == '__main__':
    nums = [5,6,2,7,4]
    print(Solution().maximumP(nums))