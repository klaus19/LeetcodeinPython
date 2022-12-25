import math


class Solution(object):

    def uniquePaths(self, m, n):
        m, n = m - 1, n - 1

        return math.factorial(m + n) // math.factorial(m) // math.factorial(n)


if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))
