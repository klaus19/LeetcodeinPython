import heapq


class Solution(object):
   def lastStoneWeight(self,stones):
    heap = []
    # Convert to negative values, so we can use a max heap
    for stone in stones:
        heapq.heappush(heap, -stone)
    while len(heap) > 1:
        x = -heapq.heappop(heap)
        y = -heapq.heappop(heap)
        if x != y:
            heapq.heappush(heap, -(y - x))
    if len(heap) == 0:
        return 0
    else:
        return -heap[0]


if __name__ == "__main__":
    lt =[2,7,4,1,8,1]
    print(Solution().lastStoneWeight(lt))
