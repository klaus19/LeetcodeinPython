class Solution(object):

    def duplicate(self,nums):
        nums.sort()
        for i in range(1,len(nums)):
             if nums[i] == nums[i-1]:
                 return True

        return False


if __name__ == "__main__":
    pt = [1, 2, 3, 1]
    print(Solution().duplicate(pt))

