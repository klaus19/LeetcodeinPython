class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        res =[]
        for num in nums:
            ans = a*num*num + b*num + c
            res.append(ans)

            res.sort()
        return res

if __name__ == "__main__":
    nums =[-4,-2,2,4]
    a,b,c = 1,3,5
    print(Solution().sortTransformedArray(nums, a, b, c))