class Solution(object):

    def forloop(self,nums):

        n=len(nums)
        sum =0

        for i in range(n-2,-1,-1):
            sum +=nums[i]

        return sum

if __name__ == '__main__':
    NUMS = [1,2,3,4]
    print(Solution().forloop(NUMS))