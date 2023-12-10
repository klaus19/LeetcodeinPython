class Solution(object):

    def unique_paths(self,m, n):
        # Create a 2D list to store the number of unique paths for each cell
        dp = [[0] * n for _ in range(m)]

        # Initialize the first row and first column with 1
        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        # Build the dp array using the recursive relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The final result is stored in the bottom-right cell
        return dp[m - 1][n - 1]

if __name__ == '__main__':
    # Example usage:
    m = 3
    n = 3

    print(Solution().unique_paths(m,n))

