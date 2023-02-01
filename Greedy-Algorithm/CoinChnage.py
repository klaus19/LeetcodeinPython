#Given a target amount V cents and a list of denominations of n coins, i.e. we have coinValue[i] (in cents) for coin
   # types i from [0...n - 1], what is the minimum number of coins that we must use to represent amount V?

class Solution(object):

    def minCoins(self,V, coinValue):
        n = len(coinValue)
        count = 0
        for i in range(n - 1, -1, -1):
            while V >= coinValue[i]:
                V -= coinValue[i]
                count += 1
        return count

