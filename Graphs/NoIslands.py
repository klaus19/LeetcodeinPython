class Solution(object):

    def calculate(self,grid):

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(row,col):
            if row <0 or row == rows or col < 0 or col == cols:
                return

            if grid[row][col] != '1':
                return

            grid[row][col] = 'V'

            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)


        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == '1':
                    dfs(row,col)
                    count += 1

        return count



