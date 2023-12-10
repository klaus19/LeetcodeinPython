class Solution(object):
    def countTriplets(self,arr, r):
        potential_middle = {}
        potential_end = {}
        count = 0

        for num in arr:
            # Update count for potential end elements
            if num in potential_end:
                count += potential_end[num]

            # Update potential end elements
            potential_end[num * r] = potential_end.get(num * r, 0) + potential_middle.get(num, 0)

            # Update potential middle elements
            potential_middle[num * r] = potential_middle.get(num * r, 0) + 1

        return count

if __name__ == '__main__':
    nums = [1,4,16,64]
    r =4
    print(Solution().countTriplets(nums, r))
