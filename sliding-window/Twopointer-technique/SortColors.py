class Solution(object):
    def sortColors(self,nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:  # If current element is red (0)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # If current element is white (1)
                mid += 1
            else:  # If current element is blue (2)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == '__main__':
    arr= [1,0,2,1,1,0]
    Solution().sortColors(arr)
    print(arr)


