class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
