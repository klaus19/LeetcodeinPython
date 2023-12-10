class Solution(object):

    def fibonacci(self,n,memo={}):

        if n <=1:
            return n

        if n not in memo:
            memo[n] = self.fibonacci(n-1,memo) + self.fibonacci(n-2,memo)

        return memo[n]

if __name__ == "__main__":
    n=4
    print(Solution().fibonacci(n))