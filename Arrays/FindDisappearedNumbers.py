from collections import Counter


class Solution(object):
    def findDisappearedNumbers(self, nums):
        d= Counter(nums)
        temp=[]
        for i in range(1,len(nums)+1):
            if d[i] ==0:
                temp.append(i)
        return temp

if __name__ == '__main__':
    arr = [4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(arr))