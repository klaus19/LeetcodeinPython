class Solution(object):

    def  buySell(self,prices):


        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit

if __name__ == '__main__':
    st = [7,1,5,3,6,4]
    pt = [7,6,4,3,1]
    print(Solution().buySell(st))
    print(Solution().buySell(pt))