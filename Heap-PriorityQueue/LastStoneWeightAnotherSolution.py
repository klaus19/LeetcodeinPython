import heapq
from heapq import heappop, heapify
from typing import List


class Solution(object):

    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapify(s)
        while len(s) > 1:
            heapq.heappush(s, -abs(heappop(s) - heappop(s)))
        return -s[0]

if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))  # The time complexity of this solution is also O(nlogn) and space complexity is also O(n).

