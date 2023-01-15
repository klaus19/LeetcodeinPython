class Solution(object):

    def count_change(self,money, coins):
        dp = [1] + [0] * money
        for coin in coins:
            for x in range(coin, money + 1):
                dp[x] += dp[x - coin]
        return dp[money]

if __name__ == '__main__':
    mon=4
    arr = [1,2]
    print(Solution().count_change(mon, arr))