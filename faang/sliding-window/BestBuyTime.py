from typing import List


class Solution(object):

    def max_profit(self, prices:List[int])->int:
        l, r = 0, 1  # left=buy and right=sell

        maxP = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l =r
            r += 1

        return maxP


if __name__ == "__main__":
    pt = [7, 1, 5, 3, 6, 4]
    print(Solution().max_profit(pt))
