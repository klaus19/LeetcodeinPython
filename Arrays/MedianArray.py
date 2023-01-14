class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums1.extend(nums2)
        nums1.sort()

        if len(nums1)%2 ==0:
            a = len(nums1)//2
            return float(nums1[a]+nums1[a-1])/float(2)
        else:
            a = len(nums1) // 2
            return float(nums1[a])

if __name__ == "__main__":
    p = [1,3]
    t = [2.4]
    print(Solution().findMedianSortedArrays(p,t))