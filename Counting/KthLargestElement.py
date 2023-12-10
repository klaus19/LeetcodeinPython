import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k=2
    print(Solution().findKthLargest(nums, k))