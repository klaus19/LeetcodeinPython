class Solution(object):

    def unique_paths(self, m, n, memo={}):
        key = str(m) + "-" + str(n)
        if key in memo:
            return memo[key]
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0

        memo[key] = self.unique_paths(m - 1, n, memo) + self.unique_paths(m, n - 1, memo)
        return memo[key]

if __name__ == "__main__":
    m, n = 3, 3
    print(Solution().unique_paths(m, n))
