class Solution(object):
    def threeSum(self, nums):
        res = []  # List to store unique triplets that sum to zero
        nums.sort()  # Sort the input array for efficient two-pointer technique

        for i in range(len(nums) - 2):  # Iterate through the array as the potential first element
            # Skip duplicate values as the potential first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Initialize two pointers for the remaining elements

            while left < right:
                threesum = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet

                if threesum > 0:
                    right -= 1  # Move the right pointer to decrease the sum
                elif threesum < 0:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    # Found a valid triplet with sum zero, add it to the result
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values on both sides to avoid duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # Move the left pointer
                    right -= 1  # Move the right pointer

        return res  # Return the list of unique triplets that sum to zero

if __name__ == "__main__":
    arr=[-1,0,1,2,-1,-4]
    print(Solution().threeSum(arr))

    # Amazon,Google,Apple, Adobe, Facebook,Microsoft,Oracle,Uber,Tesla,LinkedIn,IBM
    # The time complexity of the given "3Sum" solution with proper comments is still O(n^2), where "n" is the number of elements in the nums array.
    #
    # The comments added to the code provide explanations for each part,
    # but they do not change the underlying time complexity analysis, which remains as follows:
    #
    # Sorting the nums array takes O(n * log(n)) time.
    #
    # After sorting, the code uses two nested loops:
    #
    # The outer loop iterates over each element of the array once (up to len(nums) - 2 times),
    # which is O(n) iterations.
    # The inner while loop (two-pointer technique) also takes O(n) time in total across all iterations combined.
    # Since the inner while loop is nested inside the outer loop, the overall time complexity is O(n) * O(n) = O(n^2).
    # The space complexity of the given "3Sum" solution is O(n), where "n" is the number of elements in the nums array.
    #
    # Here's why the space complexity is O(n):
    #
    # The primary space-consuming data structure in the code is the res list,
    # which stores the unique triplets that sum to zero. In the worst case, when there are many such triplets, this list can grow to contain O(n) triplets. Each triplet itself contains three elements.
    #
    # Other variables used in the code, such as loop indices (i, left, right),
    # are of constant space, as they do not depend on the size of the input array.
    #
    # Therefore, the space complexity is dominated by the space required to store the res list,
    # making it O(n) in the worst case when there are many valid triplets that sum to zero.

