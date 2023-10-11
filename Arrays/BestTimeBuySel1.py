class Solution(object):
    def maxProfit(self, prices):

        l=0
        r=1
        max_profit =0

        while r<len(prices):
            curr_profit = prices[r]-prices[l]

            if prices[l]<prices[r]:
                max_profit = max(max_profit,curr_profit)
            else:
                l = r
            r+=1
        return max_profit

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    print(Solution().maxProfit(nums))
