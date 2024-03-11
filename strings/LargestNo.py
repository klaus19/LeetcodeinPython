class Solution(object):
    def largestNumber(self, nums):
        final_no = ""

        for i in range(len(nums)):
            curr_max = max(nums)
            final_no +=str(curr_max)
            nums.remove(curr_max)
        return final_no

if __name__ == "__main__":
    no = [10,2]
    print(Solution().largestNumber(no))