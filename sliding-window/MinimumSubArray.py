class Solution(object):

    def min_subarray_length(self,nums, target):
        if not nums:
            return 0

        left = 0
        min_length = float('inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0




if __name__ == '__main__':

    arr,tar = [2, 3, 1, 2, 4, 3], 7
    print(Solution().min_subarray_length(arr,tar))