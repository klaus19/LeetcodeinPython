class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res = []
        res.extend(nums1)
        res.extend(nums2)

        res.sort()
        lo = 0
        hi = len(res) - 1

        mid = lo + (hi - lo) // 2

        if len(res) % 2 == 0:
            # Previously, you just took the average of two elements
            # at mid and mid + 1. This is incorrect for even-length arrays.
            # Instead, we need to consider both elements.
            alpha = (res[mid] + res[mid + 1]) / 2.0
            answer = alpha
        else:
            # For odd-length arrays, taking the middle element is correct.
            alpha = float(res[mid])
            answer = alpha

        return answer

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1,nums2))
