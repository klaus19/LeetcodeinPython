class Solution(object):

    def richest(self,accounts):

        customers = len(accounts)
        banks = len(accounts[0])
        maxSum=0

        for customer in range(customers):
            currSum=0
            for bank in range(banks):
               currSum+=accounts[customer][bank]

            maxSum = max(maxSum,currSum)

        return maxSum

if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(Solution().richest(accounts))


