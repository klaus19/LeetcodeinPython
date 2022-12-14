import sys


class Solution(object):

    sys.setrecursionlimit(15000)
    def integerReplacement(self, n, counter=0):

        if not n % 2:
            return self.integerReplacement(n / 2, counter + 1)
        else:
            return min(self.integerReplacement(n + 1, counter + 1), self.integerReplacement(n - 1, counter + 1))


if __name__ == "__main__":
    c = 0
    no = 8
    print(Solution().integerReplacement(no, c))
