class Solution:
    def largest_three_numbers(self, nums):
        if len(nums) < 3:
            return sorted(nums, reverse=True)

        largest_nums = nums[:3]
        largest_nums.sort(reverse=True)

        for num in nums[3:]:
            if num > largest_nums[2]:
                largest_nums[0], largest_nums[1], largest_nums[2] = largest_nums[1], largest_nums[2], num
            elif num > largest_nums[1]:
                largest_nums[0], largest_nums[1], = largest_nums[1], num
            elif num > largest_nums[0]:
                largest_nums[0] = num

        return largest_nums


lt = [10, 5, 20, 7, 9]
print(Solution().largest_three_numbers(lt))  # Output: [20, 10, 9]
