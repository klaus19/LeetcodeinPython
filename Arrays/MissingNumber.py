class Solution(object):
    def missingNumber(self, nums):

        nums.sort()  # Corrected the sorting

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        # If no missing number found, return the next number
        return len(nums)

if __name__ == "__main__":
    nums =[3,0,1]
    print(Solution().missingNumber(nums))



