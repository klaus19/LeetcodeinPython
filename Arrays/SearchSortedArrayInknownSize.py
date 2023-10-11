class Solution(object):
    def search(self, reader, target):

        l=0
        r=10000

        while l<=r:
            mid = (l+r)//2
            val = reader.get(mid)
            if val ==target:
                return mid
            elif val < target:l = mid+1
            else: r = mid-1
        return -1
