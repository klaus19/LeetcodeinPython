class Solution(object):
    def findErrorNums(self,nums):
       n = len(nums)
       a = sum(nums)
       b = sum(set(nums))
       c = (n * (n + 1)) // 2

       return [a - b, c - b]


if __name__ == '__main__':
    arr = [1,2,2,4]
    Solution().findErrorNums(arr)
    print(arr)

