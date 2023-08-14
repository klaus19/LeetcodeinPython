class Solution(object):

    def maxProfit(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left +=1
            right += 1
        return max_profit

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))