# Asked in amazon,microsoft, google, bloomberg

class Solution(object):

    def best_time(self, prices):
        min_price, profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


if __name__ == '__main__':
    ltr = [7, 1, 5, 3, 6, 4]
    print(Solution().best_time(ltr))   # the output is 5
