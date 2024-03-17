from heapq import heapify, heappop, heappush


class Solution(object):
    def findContentChildren(self, g, s):
        heapify(g)
        heapify(s)
        ans=0
        while g and s:
            hunger = heappop(g)
            size = heappop(s)
            if size >=hunger:
                ans+=1
                continue
            heappush(g,hunger)
        return ans

if __name__ == '__main__':
    g = [1, 2, 3]
    s =[1,1]
    print(Solution().findContentChildren(g, s))