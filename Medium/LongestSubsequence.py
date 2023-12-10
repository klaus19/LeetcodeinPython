class Solution(object):

    def longestConsecutive(self, nums):
        nums.sort()
        longest=0
        curr_long = min(1,len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                curr_long+=1

            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(longest, curr_long)
        return longest

if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))