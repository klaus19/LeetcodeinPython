class Solution(object):
      def staircase(self,n):
          for i in range(1, n + 1):
        # Print spaces before the '#' characters
               spaces = ' ' * (n - i)

        # Print the '#' characters for the current row
               hashtags = '#' * i

        # Combine spaces and hashtags and print the row
               row = spaces + hashtags



if __name__ == '__main__':
    n=4
    print(Solution().staircase(n))