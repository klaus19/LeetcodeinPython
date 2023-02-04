import heapq
from collections import Counter


class Solution(object):

    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == '__main__':

    lt = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(lt,k))
