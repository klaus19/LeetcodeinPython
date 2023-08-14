class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        n=len(prices)

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit+=prices[i]-prices[i-1]
        return maxProfit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))

# Mostly asked in Microsoft,Apple, Uber, Google,Amazon,Adobe, Facebook ,Bloomberg
#The time complexity of the maxProfit function in your provided code is O(n), where n is the number of elements in the prices array.
# This is because the code iterates through the prices array once, visiting each element exactly once.
# The space complexity of the maxProfit function in your provided code is O(1),
# which means it uses a constant amount of extra space regardless of the size of the input array.