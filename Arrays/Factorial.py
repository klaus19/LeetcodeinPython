from math import factorial


class Solution(object):

    def factorial(self,n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    result = factorial(5)
    print("Factorial of 5 is:", result)

if __name__ == '__main__':
    n=5
    print(Solution().factorial(n))