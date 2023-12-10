class Solution(object):

    # Python3 program to count
    # subarrays having product
    # less than k.

    def countSubArrayProductLessThanK(self,a, k):
        n = len(a)
        p = 1
        res = 0
        start = 0
        end = 0
        while (end < n):
            p *= a[end]
            while (start < end and p >= k):
                p = int(p // a[start])
                start += 1
            if (p < k):
                l = end - start + 1
                res += l

            end += 1

        return res

if __name__ == "__main__":
    nums =[1, 2, 3, 4]
    k=10
    print(Solution().countSubArrayProductLessThanK(nums,k))






