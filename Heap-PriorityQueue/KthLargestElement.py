import heapq


class Solution(object):

    def kThLargest(self,arr,k):
        heap=[]
        for num in arr:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

if __name__ == '__main__':
    nums =[3,2,1,5,6,4]
    k=2
    print(Solution().kThsmallest(nums,k))