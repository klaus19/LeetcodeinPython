class Solution(object):

    def largestPerimeter(self,nums):

        nums.sort(reverse=True)
        max_peri = 0

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                max_peri = max(max_peri, nums[i] + nums[i + 1] + nums[i + 2])

        return max_peri

if __name__ == '__main__':
    arr = [1,2,1,10]
    print(Solution().largestPerimeter(arr))
