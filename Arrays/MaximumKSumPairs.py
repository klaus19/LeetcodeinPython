class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        nums.sort()  # Sort the input list

        left, right = 0, len(nums) - 1
        if not nums:
            return 0

        if len(nums) ==1:
            return 0


        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return count

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    k = 5
    print(Solution().maxOperations(arr, k))

#Sorting: Sorting the nums list has a time complexity of O(n * log(n)), where 'n'
# is the length of the input list. Sorting dominates the time complexity in this algorithm.

#Two-Pointer Traversal: After sorting, you iterate through the nums list using
# the two-pointer technique, which takes O(n) time in the worst case because both the left and
# right pointers traverse the list once.
#