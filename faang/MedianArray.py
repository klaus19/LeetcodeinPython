class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = []
        s = 0
        for v in nums1:
            l.append(v)

        for i in nums2:
            l.append(i)

        l = sorted(l)
        print(l)

        if (len(l) % 2) == 0:
            while len(l) > 2:
                l.pop(0)
                l.pop(-1)

        else:
            while len(l) > 1:
                l.pop(0)
                l.pop(-1)

        for a in l:
            s += a

        return float(s) / (len(l))


if __name__ == "__main__":
    n1 = [1, 3]
    n2 = [2]
print(Solution().findMedianSortedArrays(n1,n2))