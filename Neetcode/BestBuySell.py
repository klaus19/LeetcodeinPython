class Solution(object):
    def bestbuy(self,prices):

        l,r=0,1 # l=buy, r = sell
        maxP=0

        while r<len(prices):
            # profitable?
            if prices[l]<prices[r]:
               profit = prices[r]-prices[l]
               maxP = max(maxP,profit)
            else:
               l = r
            r = r+1
        return maxP

if __name__ == "__main__":
    pt = [7,1,5,3,6,4]
    print(Solution().bestbuy(pt))