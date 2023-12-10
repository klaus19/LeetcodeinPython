class Solution(object):
    def totalMoney(self, n):
        amount = 0
        i=1

        while i < n+1:
            amount +=i

            i+=1
        return amount

if __name__ == '__main__':
    n=4
    print(Solution().totalMoney(n))
